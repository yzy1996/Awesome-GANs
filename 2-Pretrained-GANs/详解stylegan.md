参考资料：

https://zhuanlan.zhihu.com/p/63230738



首先是有一个 mapping network，得到一个比Z空间更好的W空间

在文章中也分析了Z空间和W空间分别的解耦能力



### 模型的特殊设计

- 正则化-混合正则化（mixing regularization）

对给定比例的训练样本（随机选取）使用样式混合的方式生成图像。在训练过程中，使用两个随机隐码z（latent code）而不是一个，生成图像时，在合成网络中随机选择一个点（某层），从一个隐码切换到另一个隐码(称之为样式混合)。具体来说，通过映射网络运行两个潜码z1、z2，并让对应的w1、w2控制样式，使w1在交点前应用，w2在交点后应用。

这种正则化技术防止网络假设相邻样式是相关的，随机切换确保网络不会学习和依赖于级别之间的相关性。









为了控制生成特征，通过分别修改每一层的输入，不影响其他层级





StyleGAN1存在水滴问题，不仅图片中有，而且 feature map中也有

最后发现是AdaIN层导致的问题，因为IN是per-channel的，层与层之间的关系没有考虑

同时，作者注意到，std control 其实就是将feature map (per channel) 进行了一个放缩而已。这个操作可以被放到卷积层里，具体表现就是给卷积核乘以这些放缩参数（在paper中被称为weight demodulation）。





网络的层



## Tricks

Equalized Learning Rate 均衡学习率 >>> 稳定训练，提升高分辨率质量 

https://personal-record.onrender.com/post/equalized-lr/







The StyleGAN/StyleGAN2 generation process involves a number of latent spaces:

- $\mathcal{Z}$ Space
- $\mathcal{W}$ Space
- $\mathcal{W}+$ Space
- $\mathcal{S}$ Space



$\mathcal{W}+$ is mainly used for style mixing and image inversion.





几个疑问：

什么是 channel-wise activation statistics (means and variances)



## Background

> 都是作用在channel-wise activation statistics.

- BigGAN uses class-conditional BatchNorm

- StyleGAN uses AdaIN to modulatechannel-wise means and variances

- StyleGAN2 controlschannel-wise variances by modulating the weights ofthe convolution kernels



> 过去的经验，怎么解耦的效果比较好呢？

- the intermediatelatent space is more disentangled than the initialone



## Space

`latent space W` StyleGAN, StyleGAN2

`latent space W+` Image2StyleGAN

`latent space S` StyleSpace Analysis



StyleGAN2 分辨率 1024*1024，有18层layers

W是512维

W+是9216维

S是9088维，





首先是一个关于DCI (disentanglement | completeness | informativeness) metrics 





## Literature



> W+

A style-basedgenerator architecture for generative adversarial networks

Analyzing and improvingthe image quality of StyleGAN

Indomain GAN inversion for real image editing

主要用在style-mixing and image-inversion





perceptual loss







## Code

如何获得W空间



Z空间就直接随机生成就好了，10000张图

```python

```



参考[interfacegan](https://github.com/genforce/interfacegan)





The demodulation operation is a substitute for instance normalization

retain the relative magnitude between channels.

truncation tricks











**解读 StyleSpace Analysis**

<img src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/image-20220410163940204.png" alt="image-20220410163940204" style="zoom:50%;" />

核心是要找到一个新的S空间，而这个空间是怎么找出来的呢





学习 stylegan 

https://nn.labml.ai/gan/stylegan/index.html 代码详细解读



理解里面的几个步骤，是关于instantce normalization







1. 先有一个预训练好的stylegan2模型
2. 采样500K个latent vector z
3. 计算这些z对应的w和s vectors，以及图像images
4. 用40类的分类器，对这些图片打分







```python
latent_w = generator.get_latents(latent_z)



```
