# <p align=center>`Style Transfer`</p>

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 

A collection of resources on Image Style Transfer (photorealistic image stylization) and Image-to-image (i2i) translation,



<details><summary><b>Contributing</b></summary><p>

Feedback and contributions are welcome! If you think I have missed out on something (or) have any suggestions (papers, implementations and other resources), feel free to pull a request or leave an issue. I will release the [latex-pdf version]() in the future. :arrow_down:markdown format:

``` markdown
[Paper Name](abs link)  
*[Author 1](homepage), Author 2, and Author 3*
**[`Conference/Journal Year`] (`Institution`)** [[Github](link)] [[Project](link)]
```

:smile: Now you can use this [script](https://github.com/yzy1996/Python-Code/tree/master/Python%2BarXiv) to automatically generate the above text.

</p></details>

## Introduction

**Unsupervised image-to-image translation (UNIT)** aims to translate images from one domain to another without paired data.



Photorealistic image stylization aims at changing style of a photo to that of a reference photo with the constraint that the stylized photo should remain photorealistic.

learn translations between domains, applying to the context of source images a target appearance learned from a dataset.



It has attracted increasing attentions since its widely practical use, such as 

- colorization

- super resolution

- semantic synthesis

- domain adaption



在风格迁移里有一个专门的Loss叫perceptual loss，最早是在  Perceptual losses for real-time style transfer and super-resolution 2016 里被提出

related papers:

`citation 4258` Perceptual losses for real-time style transfer and super-resolution

`citation 2431` Image Style Transfer Using Convolutional Neural Networks

`citation 698` Generating images with perceptual similarity metrics based on deep networks



后来在很多图像里得到应用

- 超分辨率：

  Image Super-Resolution by Neural Texture Transfer 2019

  Super-resolution with deep convolutional sufficient statistics 2016

  Photo-realistic single image super-resolution using a generative adversarial network 2017

  EnhanceNet: Single image super-resolution through automated texture synthesis 2017



## Literature

> The order is from the old to the latest

[Image-to-Image Translation with Conditional Adversarial Networks](https://openaccess.thecvf.com/content_cvpr_2017/papers/Isola_Image-To-Image_Translation_With_CVPR_2017_paper.pdf)  
*Phillip Isola Jun-Yan Zhu Tinghui Zhou Alexei A. Efros*  
**[`CVPR 2017`]**

[Image style transfer using convolutional neural networks](https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Gatys_Image_Style_Transfer_CVPR_2016_paper.html)  
*Leon A. Gatys, Alexander S. Ecker, Matthias Bethge*  
**[`CVPR 2016`]**	**(`Tubingen`)**

[Unsupervised Image-to-Image Translation Networks](https://arxiv.org/pdf/1703.00848)  
*Ming-Yu Liu, Thomas Breuel, Jan Kautz*  
**[`NeurIPS 2017`] ()**

[Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/pdf/1703.10593)  
*Jun-Yan Zhu, Taesung Park, Phillip Isola, Alexei A. Efros*  
**[`ICCV 2017`] (`UCB`)**

[A Closed-form Solution to Photorealistic Image Stylization](https://arxiv.org/abs/1802.06474)  
*Yijun Li, Ming-Yu Liu, Xueting Li, Ming-Hsuan Yang, Jan Kautz*  
**[`ECCV 2018`]**	**(`UC, NVIDIA`)**	[[Github](https://github.com/NVIDIA/FastPhotoStyle)]

[CoMoGAN: continuous model-guided image-to-image translation](https://arxiv.org/abs/2103.06879)  
*Fabio Pizzati, Pietro Cerri, Raoul de Charette*  
**[`CVPR 2021 (oral)`]**	**(`Inria`)**	[[Github](https://github.com/cv-rits/CoMoGAN)]





