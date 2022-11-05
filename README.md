# <p align=center>`awesome Generative Adversarial Networks (GANs)`</p>

A collection of resources on Generative Adversarial Networks (GANs).



## Table of Contents

- [Introduction](#Introduction)

- [1. Basic Knowledge](#Basic-Knowledge)

- [2. Research Branch](#Research-Branch)



## Introduction

The purpose of GAN is to generate/synthesize fake but photo-real images (synthesize high-resolution portraits that are often indistinguishable from real faces). GANs are popular partly because they tackle the important unsolved challenge of unsupervised learning. It represents a zero-sum game between two machine players, a generator and a discriminator, designed to learn the distribution of data.  Using an adversarial methods, bypass the need of computing densities, at the expense of a good density estimation.

If intelligence was a cake, unsupervised learning would be the cake, supervised learning would be the icing on the cake, and reinforcement learning would be the cherry on the cake. We know how to make the icing and the cherry, but we don’t know how to make the cake. – Yann LeCun, 2016.

**To quickly touch GAN:** [Stylegan Online Demo](https://thispersondoesnotexist.com/)

**To read some related survey:** [2019](https://arxiv.org/abs/1906.01529) [2020](https://arxiv.org/abs/2001.06937) 

**SOTA Benchmark:** [Image Generation](https://paperswithcode.com/task/image-generation) 

![GAN Development](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/GAN%20Development.png)



## Basic Knowledge

- **mode collapse**: diversity the generator can only learn some limited patterns from the large-scale target datasets, or assigns all of its probability mass to a small region in the space.

- **vanishing gradient**: the gradient of generator vanishes at the begining of training process.



See more details in the subfolders.

- [Classical GANs](./1-Classical-GANs)

- [Conditional GAN](1-Conditional-GAN)

- [Evaluation Metrics](./1-Evaluation-Metrics)
- [GANs Comparation](./1-GANs-Comparation)
- [Training Strategy](./Training-Strategy )



## Research Branch

|                            Branch                            |                                                              |
| :----------------------------------------------------------: | ------------------------------------------------------------ |
|           [Controllable-GAN](./2-Controllable-GAN)           | **Inverion**. We can find a common latent code, and we can also find a seperate code for each layer of the generator. It is easy and better to manipulate a given image in the latent feature space. |
|     [Few-Shot & Limited Data](./2-Few-Shot-Limited-Data)     |                                                              |
|            [Pretrained GANs](./2-Pretrained-GANs)            |                                                              |
| [Style Transfer & Image2Image](./2-Style-Transfer-Image2Image) |                                                              |
|         [Other Applications](./3-Applicational-GAN)          | In&Out painting, Text2image, High&Super Reselution, Animation, Video Generation |



## Some Awesome Codes

[studioGAN](https://github.com/POSTECH-CVLab/PyTorch-StudioGAN)
