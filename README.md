# <p align=center>`awesome Generative Adversarial Networks (GANs)`</p>

> This repo is to help underistand the principle of GANs.



The purpose of GAN is to generate/synthesize fake but photo-real images.

We can extract it as 

Because it's a complex distribution, it's hard to directly get the true distribution of the dataset



Since GANs invention, it has yield impressive results, especially for image generation.

Recent work can synthesize random high-resolution portraits that are often indistinguishable from real faces.



Generative models aim to approximate samples from a complex high-dimensional target distribution $\mathbb{P}$. 

The adversarial mechanism reflects by a generator and a discriminator who compete against each other. Unlike other deep neural network models trained with a loss function until convergence, GAN train these two together to maintain a equilibrium finally.

The generator learns to map from a low-dimension space $\mathcal{Z}$ to a high-dimension space $\mathcal{X}$ with a model distribution $\mathbb{Q}$.

The discriminator learns to accurately distinguish between the synthesized data $\mathbf{Y}$ coming from $\mathbb{Q}$ and the real data $\mathbf{X}$ from $\mathbb{P}$. 

We can denote by $\mathbb{P}$ and $\mathbb{Q}$ the data and model distribution, respectively.



Generative Adversarial Network (GAN) is formulated as a two-player game between a gnerator (G) and a discriminator (D), where G targets at reproducing the distribution of observed data through synthesising new samples, and D competes with G by distinguishing the generated images from the real ones. In priciple, they are expected to reach an equilibrium where D cannot tell the real and fake images apart.



GAN use the reparametrization trick to sample from a complex probability distribution by learning a transformation $y=f(x), x\sim N(0, I)$, where f is the transformatioin function modelled by a neural network.



**Application**

Super-resolution, colorisation, text-guided generation



## SOTA

https://paperswithcode.com/task/image-generation

https://paperswithcode.com/sota/image-generation-on-lsun-bedroom-256-x-256



## Training Strategy

- [Projected GANs Converge Faster](https://arxiv.org/pdf/2111.01007.pdf)  
  *Axel Sauer, Kashyap Chitta, Jens Müller, Andreas Geiger*  
  **[`NeurIPS 2021`] (`MPI`)** [[Code](https://github.com/bryandlee/animegan2-pytorch)]



$z$ is a distribution and $x$ is a distribution and $x^{\prime}$ is also a distribution



 high-dimensional 



integral probability metrics (IPMs)

> a “well behaved” function with large amplitude where $P_x$ and$P_z$ differ most

- Wasserstein IPMs



Maximum Mean Discrepancies (MMDs)

> the critic function is a member of a reproducing kernel Hilbert space







- [On gradient regularizers for MMD GANs](https://arxiv.org/pdf/1805.11565.pdf)  
  *Michael Arbel, Danica J. Sutherland, Mikołaj Bińkowski, Arthur Gretton*  
  **[`NeurIPS 2018`] (`UCL`)**





## Pre-trained 

- [When, Why, and Which Pretrained GANs Are Useful?](https://openreview.net/pdf?id=4Ycr8oeCoIh)  
  *Anonymous*  
  **[`ICLR 2022 submit`]**



