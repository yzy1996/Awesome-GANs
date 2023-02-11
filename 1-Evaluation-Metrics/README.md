<h1 <p align=center>GAN Evaluation</h1>

Evaluating the performance of GANs: heuristic metrics such as the Inception score (IS) and Fréchet Inception Distance (FID).



## Introduction

生成模型的本质是希望学习拟合一个真实图像数据分布的参数，其实就是likelihood，如果能刻画似然，那么就可以直接计算，越大越好。但GAN这样的隐式模型无法直接计算似然函数；关于GAN评价的重要性不言而喻，最简单的当然就是人工用眼判断真假 (Manual GAN Evaluation)，毕竟生成模型的目标就是能够以假乱真。在文献中一些比较主流的评价指标有：

**Inception Score (IS):** `越大越好` [论文](https://arxiv.org/abs/1606.03498) - 用一个训练好的分类器 (Inception v3) 对生成的图像做分类 (一共有1000类)，计算公式为：
$$
\mathrm{IS}=\exp \left(\mathbb{E}_{x \sim p_{g}} D_{K L}(p(y \mid x) \| p(y))\right)
$$
where $x \sim p_g$ is a generated image, $p(y|x)$ is the conditional class distribution computed via the inception network, and $p(y) P(y) = \int_{z} p(y \mid x=G(z)) d z$ is the marginal class distribution.

> 因为我们是根据真实数据生成的样本，而原数据是带有类别标签的，所以我们可以通过新生成的数据是否能被很好的判断出类别，来衡量生成数据的质量。 IS想抓住的特点有两点：(1) 质量 - 生成的图像被判别得越准确越好，也就是 $p(y|x)$ 应该是尽可能接近 one-hot 同时熵很低。(2) 多样性 - 生成的图像被判别的种类应该越多越好，同时每个类别的分布应该是尽可能均匀的，即生成的每个类别数量都差不多。以上两点同时最好的时候，就是IS最大的时候。



**Frechet Inception Distance (FID):**`越小越好` [论文](https://arxiv.org/abs/1706.08500) - 为了引入真实数据，没有用Inception网络的类别输出，而是使用网络某一层提取的特征（选择的是 pool_3），这样对真实数据仍适用。同时还要假设这些计算出来的特征是服从高斯分布的。真实图像得到 $\mathcal{N}(\mu_r, \Sigma_r)$，生成图像得到 $\mathcal{N}(\mu_g, \Sigma_g)$，再用Frechet距离计算：
$$
\operatorname{FID}(x, g)=\left\|\mu_{x}-\mu_{g}\right\|_{2}^{2}+\operatorname{Tr}\left(\Sigma_{x}+\Sigma_{g}-2\left(\Sigma_{x} \Sigma_{g}\right)^{\frac{1}{2}}\right)
$$

> 注意：sample 数量应该比网络层的维度大，Inception pool_3 的维度是 2048，所以应该大于 2048，一般推荐用大于 10,000 个样本。（原因是计算协方差矩阵至少得填满才能算平方根）



**Kernel Inception Distance (KID):** [论文](https://arxiv.org/abs/1801.01401) - 为了松弛高斯分布的假设，提出用一个多项kernel来计算squared Maximum Mean Discrepancy，特征还是跟上面一样不变，这样也就不需要太多的样本来计算。



$\textbf{FID}_{\infty} \ \&\ \textbf{IS}_{\infty}:$ [论文](https://arxiv.org/abs/1911.07023) - 发现FID和IS存在模型偏差，因此不同模型之间的比较就不够有说服力。



**Clean FID:** [论文]() - 因为前面这些指标，网络是一样的，意味着输入的图像尺寸得是相同的，那么不同的尺寸需要resize，而恰恰是这个操作会导致不一致性。因此这个工作提出了一种统一的方式。



补充知识：

**Kullback-Leibler divergence (KLD):** One common measure of difference between probability distributions is the Kullback-Leibler divergence (KLD), noting that it is not symmetric.
$$
KLD(p \| q)=\mathbb{E}_{x \sim p}\left[\log \left(\frac{p(x)}{q(x)}\right)\right]
$$
We refer to $KLD(p_{data}\|p_{model})$ as the KL divergence and $KL(p_{model}\|p_{data})$ the Reverse KL (RKL) divergence. It is important to note that the KL divergenceis biased towards "inclusive" models (where the model “covers" all high likelihood areas of the data distribution). The RKL has a bias toward "exclusive" models (where the model does not cover low likelihood areas of the data distribution).  –画个图说明

**MMD： RHKS 核**；Gram Matrix就是多项式核的MMD https://arxiv.org/abs/1701.01036



## Code

现有的一些好的代码仓：

- [pytorch-fid](https://github.com/mseitzer/pytorch-fid)
- [clean-fid](https://github.com/GaParmar/clean-fid)
- [LPIPS](https://github.com/richzhang/PerceptualSimilarity)
- [GAN-Metrics](https://github.com/xuqiantong/GAN-Metrics)
- [fcd](https://github.com/eyalbetzalel/fcd)



`inception-2015-12-05.pt` is a torchscript model of the pre-trained Inception-v3 network

需要注意的是，FID的计算受到数据的影响很大，应该满足Inception的输入要求，例如图像尺寸应该是299，同时应该变到0-1。



## Literature

- [Sinkhorn Distances: Lightspeed Computation of Optimal Transportation Distances](https://arxiv.org/abs/1306.0895)  
  **[`arXiv 2013`]** *Marco Cuturi* 

- [A note on the evaluation of generative models](https://arxiv.org/abs/1511.01844)  
  **[`arXiv 2015`]** *Lucas Theis, Aäron van den Oord, Matthias Bethge* 

- [Generating Images with Perceptual Similarity Metrics based on Deep Networks](https://arxiv.org/abs/1602.02644)  
  **[`arXiv 2016`]** *Alexey Dosovitskiy, Thomas Brox* 

- [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://arxiv.org/abs/1603.08155)  
  **[`arXiv 2016`]** *Justin Johnson, Alexandre Alahi, Li Fei-Fei* 

- [GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium](https://arxiv.org/abs/1706.08500)  
  **[`arXiv 2017`]** *Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, Sepp Hochreiter* 

- [A Note on the Inception Score](https://arxiv.org/abs/1801.01973)  
  **[`ICML 2018`]** *Shane Barratt, Rishi Sharma* 

- [An empirical study on evaluation metrics of generative adversarial networks](https://arxiv.org/abs/1806.07755)  
  **[`arXiv 2018`]** *Qiantong Xu, Gao Huang, Yang Yuan, Chuan Guo, Yu Sun, Felix Wu, Kilian Weinberger* 

- [Pros and Cons of GAN Evaluation Measures](https://arxiv.org/abs/1802.03446)  
  **[`arXiv 2018`]** *Ali Borji* 

- [The Unreasonable Effectiveness of Deep Features as a Perceptual Metric](https://arxiv.org/abs/1801.03924)  
  **[`CVPR 2018`]** *Richard Zhang, Phillip Isola, Alexei A. Efros, Eli Shechtman, Oliver Wang* 
