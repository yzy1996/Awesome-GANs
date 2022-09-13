<span id="image2styleGAN"></span>
[How to Embed Images Into the StyleGAN Latent Space?](https://arxiv.org/pdf/1904.03189.pdf)  
**[`ICCV 2019`] (`KAUST`)**	[[Code](https://github.com/NVlabs/stylegan)]
*Rameen Abdal, Yipeng Qin, Peter Wonka*

<details><summary>Click to expand</summary><p>

> **Summary**

They propose an embedding algorithm to map a given image into the latent space of StyleGAN pre-trained on the FFHQ dataset. This embedding enables semantic image editing operations that can be applied to existing photographs. They show results for *image morphing*, *style transfer*, and *expression transfer*.

> **Details**

<div align="center">
	<img src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20210110163352.png" width="500" />
</div>

</p></details>

---



Semantic photo manipulation with a generative image prior





**[`Transforming and Projecting Images into Class-conditional Generative Networks`]**

**[`2020`]** **[`ECCV`]** [project page](https://minyoungg.github.io/pix2latent/) **[[:octocat:](https://github.com/minyoungg/pix2latent)]** 


<details><summary>Click to expand</summary><p>
![model](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20200905121749.png)
**Key words:**


> image-edit

**Problem**:

> Most methods apply only to synthetic images that are generated by GANs in the first place.
>
> 只能修改GAN生成的图片，而不能直接修改现有图片。
>
> In the real-world cases, people would like to edit their own image.

**Related work:**

> Train a network for each separate image transformation (training time & model parameters)
>
> Projection [Generative visual manipulation on the natural image manifold] [Neural photo editing with introspective adversarial networks] [Invertible conditional gans for image editing]

**Main method:**

> by searching for an appropriate latent code, we project the image to the manifold of images produced by GANs.

</p></details>