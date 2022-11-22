# Improving GANs

> 本文档的目标 noise-to-image synthesis

**G**enerator plays a mapping task to generate an RGB image

**D**iscriminator plays a bi-classification task via distinguishing real and synthesized samples. The discriminator’s task is two-fold: First, it projects the real and fake samples into a meaningful space. Second, it discriminates based on this representation.

however, the synthesized data distribution varies with the evolving generator, thus the bi-classification task has a significant distribution shift issue.

- Using pre-trained representations to improve. But strong pre-trained features enable the D to dominate the two-player game, resulting in gradients vanishing.

  feature pyramids to enable multi-scale feedback with multiple discriminators and random
  projections to better utilize deeper layers of the pretrained network.

Limited Data 一个是有这个需求，



The improvement becomes limited even negative given sufficient training data

extra computations 



Existing studies on image classification [19, 20] have pointed out, it is critical to align the model capacity to the task difficulty, otherwise the issue of either under-fitting or over-fitting occurs.





**from the generator side**

novel generator architectures

1. Spectral normalization for generative adversarial networks

2. Self-attention generative adversarial networks

3. A style-based generator architecture for generative adversarial networks

4. Analyzing and improving the image quality of StyleGAN

5. Alias-free generative adversarial networks

6. Large scale gan training for high fidelity natural image synthesis

   

**from the discriminator side**

- data augmentation alleviate the overfitting of discriminator 

主要是集中在不充分数据下的研究

那么当数据充分的时候呢

有没有增加计算复杂度

utilize an encoder-decoder discriminator 



**multiple discriminators** -> increasing computational effort.

[Stabilizing GAN Training with Multiple Random Projections](https://arxiv.org/abs/1705.07831)
*Behnam Neyshabur, Srinadh Bhojanapalli, Ayan Chakrabarti*
**[`arXiv 2017`]**

[Generative Multi-Adversarial Networks](https://arxiv.org/abs/1611.01673)
*Ishan Durugkar, Ian Gemp, Sridhar Mahadevan*
**[`ICLR 2017`]**

[Multi-objective training of Generative Adversarial Networks with multiple discriminators](https://arxiv.org/abs/1901.08680)
*Isabela Albuquerque, João Monteiro, Thang Doan, Breandan Considine, Tiago Falk, Ioannis Mitliagkas*
**[`ICML 2019`]**

[On-line Adaptative Curriculum Learning for GANs](https://arxiv.org/abs/1808.00020)
*Thang Doan, Joao Monteiro, Isabela Albuquerque, Bogdan Mazoure, Audrey Durand, Joelle Pineau, R Devon Hjelm*
**[`AAAI 2019`]**



Discriminator 更好学 to prevent overfitting of the discriminator, **differentiable augmentation** methods have recently been proposed



[On Data Augmentation for GAN Training](https://arxiv.org/abs/2006.05338)  
*Ngoc-Trung Tran, Viet-Hung Tran, Ngoc-Bao Nguyen, Trung-Kien Nguyen, Ngai-Man Cheung*  
**[`TIP 2021`] (`SUTD`)**  

[Differentiable Augmentation for Data-Efficient GAN Training](https://arxiv.org/pdf/2006.10738.pdf)  
*Shengyu Zhao, Zhijian Liu, Ji Lin, Jun-Yan Zhu, Song Han*  
**[`NeurIPS 2020`]** **(`MIT`)** [[:octocat:](https://github.com/mit-han-lab/data-efficient-gans)]

[Image Augmentations for GAN Training](https://arxiv.org/abs/2006.02595)  
*Zhengli Zhao, Zizhao Zhang, Ting Chen, Sameer Singh, Han Zhang*  
**[`TIP 2020`] (`UC Irvine, Google`)**  





[A U-Net Based Discriminator for Generative Adversarial Networks](https://arxiv.org/abs/2002.12655)
*Edgar Schönfeld, Bernt Schiele, Anna Khoreva*
**[`CVPR 2020`]**

Energy-based generative adversarial network



- [Projected GANs Converge Faster](https://arxiv.org/abs/2111.01007)  
  *Axel Sauer, Kashyap Chitta, Jens Müller, Andreas Geiger*  
  **[`NeurIPS 2021`] (`MPI`)**

> They find the discriminator cannot fully exploit features from deeper layers of the pretrained model, so they project generated and real samples into a fixed, pretrained feature space.



**incorporate regularization** 

[Consistency Regularization for Generative Adversarial Networks](https://arxiv.org/abs/1910.12027)
*Han Zhang, Zizhao Zhang, Augustus Odena, Honglak Lee*
**[`ICLR 2020`]**

[Improved Consistency Regularization for GANs](https://arxiv.org/abs/2002.04724)
*Zhengli Zhao, Sameer Singh, Honglak Lee, Zizhao Zhang, Augustus Odena, Han Zhang*
**[`AAAI 2021`]**

[Which Training Methods for GANs do actually Converge?](https://arxiv.org/abs/1801.04406)
*Lars Mescheder, Andreas Geiger, Sebastian Nowozin*
**[`ICML 2018`]**



**introduce various extra tasks** 

[Self-Supervised GANs via Auxiliary Rotation Loss](https://arxiv.org/abs/1811.11212)
*Ting Chen, Xiaohua Zhai, Marvin Ritter, Mario Lucic, Neil Houlsby*
**[`CVPR 2019`]**

[Self-supervised GAN: Analysis and Improvement with Multi-class Minimax Game](https://arxiv.org/abs/1911.06997)
*Ngoc-Trung Tran, Viet-Hung Tran, Ngoc-Bao Nguyen, Linxiao Yang, Ngai-Man Cheung*
**[`NeurIPS 2019`]**

[Training GANs with Stronger Augmentations via Contrastive Discriminator](https://arxiv.org/abs/2103.09742)
*Jongheon Jeong, Jinwoo Shin*
**[`ICLR 2021`]**

C[ontraGAN: Contrastive Learning for Conditional Image Generation](https://proceedings.neurips.cc/paper/2020/file/f490c742cd8318b8ee6dca10af2a163f-Paper.pdf)  
*Minguk Kang, Jaesik Park*  
**[`NeurIPS 2020`]**

[Dual Contrastive Loss and Attention for GANs](https://arxiv.org/abs/2103.16748)
*Ning Yu, Guilin Liu, Aysegul Dundar, Andrew Tao, Bryan Catanzaro, Larry Davis, Mario Fritz*
**[`ICCV 2021`]**

[Data-Efficient Instance Generation from Instance Discrimination](https://arxiv.org/abs/2106.04566)
*Ceyuan Yang, Yujun Shen, Yinghao Xu, Bolei Zhou*
**[`NeurIPS 2021`]**

[Improving GAN Equilibrium by Raising Spatial Awareness](https://arxiv.org/abs/2112.00718)
*Jianyuan Wang, Ceyuan Yang, Yinghao Xu, Yujun Shen, Hongdong Li, Bolei Zhou*
**[`CVPR 2022`]**

[Projected GANs Converge Faster](https://arxiv.org/pdf/2111.01007.pdf)  
*Axel Sauer, Kashyap Chitta, Jens Müller, Andreas Geiger*  
**[`NeurIPS 2021`] (`MPI`)**

[Ensembling Off-the-shelf Models for GAN Training](https://arxiv.org/abs/2112.09130)
*Nupur Kumari, Richard Zhang, Eli Shechtman, Jun-Yan Zhu*
**[`CVPR 2022`]**





