# Few-Shot & Limited Data

> See latex/pdf version for better view of citations.

The success of GANs heavily relies on big data.

Reducing the amount of training data leads to the overfitting of the discriminator -> Mode Collapse



## Introduction

On the one hand, we can utilize **transfer learning** with a pre-trained model.

On the other hand, we can 

Dynamic data-augmentation

not only the real images from the dataset but also the synthesized images by the generator



internal issues is **the overfitting of the discriminator**



## Literature

- [Progressive Augmentation of GANs](https://arxiv.org/abs/1901.10422)  
  *Dan Zhang, Anna Khoreva*  
  **[`NeurIPS 2019`] (`Bosch`)**

- [Training Generative Adversarial Networks with Limited Data](https://arxiv.org/pdf/2006.06676.pdf)  
  *Tero Karras, Miika Aittala, Janne Hellsten, Samuli Laine, Jaakko Lehtinen, Timo Aila*  
  **[`NeurIPS 2020`] (`NVIDIA`)** [[:octocat:](https://github.com/NVlabs/stylegan2-ada)]
- [Differentiable Augmentation for Data-Efficient GAN Training](https://arxiv.org/pdf/2006.10738.pdf)  
  *Shengyu Zhao, Zhijian Liu, Ji Lin, Jun-Yan Zhu, Song Han*  
  **[`NeurIPS 2020`]** **(`MIT`)** [[:octocat:](https://github.com/mit-han-lab/data-efficient-gans)]
- [On Data Augmentation for GAN Training](https://arxiv.org/abs/2006.05338)  
  *Ngoc-Trung Tran, Viet-Hung Tran, Ngoc-Bao Nguyen, Trung-Kien Nguyen, Ngai-Man Cheung*  
  **[`TIP 2021`] (`SUTD`)**  
- [Image Augmentations for GAN Training](https://arxiv.org/abs/2006.02595)  
  *Zhengli Zhao, Zizhao Zhang, Ting Chen, Sameer Singh, Han Zhang*  
  **[`Arxiv 2020`] (`UC Irvine, Google`)**  
- [Towards Faster and Stabilized GAN Training for High-fidelity Few-shot Image Synthesis](https://arxiv.org/abs/2101.04775)  
  *Bingchen Liu, Yizhe Zhu, Kunpeng Song, Ahmed Elgammal*  
  **[`ICLR 2021`] (`Rutgers`)** [[:octocat:](https://github.com/odegeasslbc/FastGAN-pytorch)] 
- [Diverse Generation from a Single Video Made Possible](https://arxiv.org/abs/2109.08591)  
  *Niv Haim, Ben Feinstein, Niv Granot, Assaf Shocher, Shai Bagon, Tali Dekel, Michal Irani*  
  **[`ECCV 2022`] (`Weizmann Institute of Science`)**
- [Data-Efficient Instance Generation from Instance Discrimination](https://arxiv.org/abs/2106.04566)  
  *Ceyuan Yang, Yujun Shen, Yinghao Xu, Bolei Zhou*  
  **[`NeurIPS 2021`] (`CUHK, Byte`)** 

- [Deceive D: Adaptive Pseudo Augmentation for GAN Training with Limited Data](https://arxiv.org/abs/2111.06849)  
  *Liming Jiang, Bo Dai, Wayne Wu, Chen Change Loy*  
  **[`NeurIPS 2021`]** [:octocat:](https://github.com/EndlessSora/DeceiveD)
