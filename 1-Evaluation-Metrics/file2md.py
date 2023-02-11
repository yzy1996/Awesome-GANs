
from urllib import request
import re
from soupsieve import match
from pathlib import Path
from PyPDF2 import PdfReader


'''
pipeline: 自动获取文件夹下的所有pdf文件, 检查更新本地pdf版本是否为最新

不要一个一个输出，先存下来，最后输出

'''
COFE = 'ICML|NIPS|NeurIPS|ICLR|CVPR|ICCV|ECCV|AAAI|IJCAI|3DV|UAI'


class Arxiv_Information():
    def __init__(self, query_title) -> None:

        query_id, _, _ = self.read_pdf(query_title)

        if re.findall(r'\d{4}.\d{5}', query_id):
            self.query_url = f'http://export.arxiv.org/api/query?id_list={query_id}'
            self.id = query_id
            
        else:
            query_title = str(str(query_title)[:-4]).replace(' ', '+')
            self.query_url = f'https://export.arxiv.org/api/query?search_query=all:{query_title}&max_results=1'
            print(self.query_url)

        self.strInf = request.urlopen(self.query_url).read().decode('utf-8')

        if re.findall(r'<entry>[\s\S]*</entry>', self.strInf): # 匹配到了内容
            

            Id = r'<id>http://arxiv.org/abs/(.*)</id>'
            Title = r'<title>([\s\S]*)</title>' # 有时候名字太长了，会换行
            Authors = r'<author>\s*<name>(.*)</name>\s*</author>'
            Year = r'<published>(\d{4}).*</published>'

            id_version = re.findall(Id, self.strInf)[0]
            id = id_version[0:-2]
            
            title = re.findall(Title, self.strInf)[0]
            title = re.sub(r'\n\s', '', title) # 去掉换行
            title_sub = re.sub(r'[^\w\s-]', '', title) # 去掉标点  

            authors = re.findall(Authors, self.strInf)
            year = re.findall(Year, self.strInf)[0]

            self.id_version = id_version
            self.id = id
            self.title = title
            self.title_sub = title_sub
            self.authors = authors
            self.year = year
            self.publish = ''
            self.affiliation = ''
            
            self.abs_url = f'https://arxiv.org/abs/{self.id}'
            self.pdf_url = f'https://arxiv.org/pdf/{self.id}'

            self.write_notes()

        else:
            pass

    def _get_publish(self):

        # 读取 txt 预定义会议名称

        # with open(r'conf_list.txt') as f:
        #     lines = [line.strip() for line in f]
        # reg = '|'.join(lines)

        # obtain form arxiv comments
        Publish = f'<arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">[\s\S]*(({COFE}).*?\d{{4}})[\s\S]*</arxiv:comment>'
        publish = re.findall(Publish, self.strInf)

        # obatin from pdf file
        Publish_pdf = f'({COFE}).*?\d{{4}}'
        # publish_pdf = re.findall(Publish_pdf, self.pdf_text)

        if publish != []:
            self.publish = publish[0][0]

            # todo 处理例如 CVPR2020 -> CVPR 2020
            # re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", text)

        else:
            # 未来对接整个互联网搜索
            self.publish = 'arXiv ' + self.year

    def _get_affiliation(self):

        # obtain from pdf file
        # 判断这个文件是否存在
        pdf_file = Path(f'{self.year}_{self.title_sub}.pdf')

        if pdf_file.exists():
            with pdf_file.open('rb') as f:
                pdf = PdfReader(f)

                first_page = pdf.getPage(0).extractText()
                first_page = first_page.split()
        
            authors1 = self.authors[0].replace(' ', '')
            self.affiliation = first_page[first_page.index(authors1) + 1]


    def write_notes(self):

        self._get_publish()
        # self._get_affiliation()

        # 组合处理
        title_url = f'[{self.title}]({self.abs_url})  '
        
        publish = f'**[`{self.publish}`]**'

        authors = ', '.join(self.authors)
        authors = f'*{authors}*'
    
        print('-', title_url)
        print(' ', publish, authors, '\n')


    # download pdf from the web
    def download(self):
  
        request.urlretrieve(self.pdf_url, f'{self.year}_{self.title_sub}.pdf')

    def read_pdf(self, filename):

        with open(filename, 'rb') as f:

            pdf = PdfReader(f)

            first_page = pdf.pages[0]
            text = first_page.extract_text()
            text_split = text.split()
            id_version_local = text_split[-5]
            id_version = id_version_local.split(':')[-1]
            id = id_version[:-2]
            version = id[-1]

        return id, version, text


## 如果需要用到pdf文件，

def update_local_version(root_dir=Path('./'), update=False):


    pdf_list = sorted(root_dir.glob('*.pdf'))
    for filename in list(pdf_list):
        with open(filename, 'rb') as f:

            pdf = PdfReader(f)

            first_page = pdf.pages[0]
            text = first_page.extract_text()
            text_split = text.split()
            id_version_local = text_split[-5]
            id = id_version_local.split(':')[-1]
            id_version = id[-1]
            information = Arxiv_Information(query_id=id)

            if information.id_version != id_version_local and update:

                for page in pdf.pages:
                    if "/Annots" in page:
                        for annot in page["/Annots"]:
                            subtype = annot.get_object()["/Subtype"]
                            if subtype == "/Highlight":
                                # 不覆盖，抛出警告
                                print('Warning: 即将替换版本存在笔记')
                            else:
                                # 替换
                                print('>>> Downloading the latest version!!!')
                                information.download()


# TODO: 添加 logging 记录
# 记录失败的，成功的

        

if __name__ == "__main__":

    root_dir = Path('./')
    pdf_list = sorted(root_dir.glob('*.pdf'))

    for file in list(pdf_list):

        Arxiv_Information(query_title=file)

