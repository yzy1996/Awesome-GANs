在下表中展示了主流的GAN Loss形式，注意正负符号，都是最小化Loss

|   Name (paper link)   |                        Loss Function                         |
| :-------------------: | :----------------------------------------------------------: |
|    **Vanilla GAN**    | $$L_D^{GAN} = -\mathbb{E}_{x \sim p_r} [\log (D(x))] - \mathbb{E}_{\tilde{x} \sim p_g} [\log (1-D(\tilde{x}))] \\L_G^{GAN} = \mathbb{E}_{\tilde{x} \sim p_g} [\log (1 - D(\tilde{x}))]$$ |
| **non-saturated GAN** | $L_D^{GAN} = -\mathbb{E}_{x \sim p_r} [\log (D(x))] - \mathbb{E}_{\tilde{x} \sim p_g} [\log (1 - D(\tilde{x}))] \\ L_G^{GAN} = -\mathbb{E}_{\tilde{x} \sim p_g} [\log (D(\tilde{x}))]$ |
|       **LSGAN**       | $L_D^{LSGAN} = -\mathbb{E}_{x \sim p_r} [(D(x)-1)^2] + \mathbb{E}_{\tilde{x} \sim p_g} [D(\tilde{x})^2] \\L_G^{LSGAN} = -\mathbb{E}_{\tilde{x} \sim p_g} [(D(\tilde{x})-1)^2]$ |
|       **WGAN**        | $$\begin{align}&L_{D}^{WGAN}=-\mathbb{E}_{x \sim p_r}[D(x)]+\mathbb{E}_{\tilde{x} \sim p_g}[D(\tilde{x})]\\&L_{G}^{WGAN}=-\mathbb{E}_{\tilde{x} \sim p_g}[D(\tilde{x})]\\&W_D \leftarrow \text{clip-by-value}(W_D, -0.01, 0.01) \end{align}$$ |
|      **WGAN-GP**      | $$L_{D}^{WGAN-GP}=L_{D}^{WGAN} + \lambda {\mathbb{E}}_{\hat{x} \sim p_{\hat{x}}}\left[\left(\left\|\nabla_{\hat{x}} D(\hat{x})\right\|_{2}-1\right)^{2}\right] \\ L_{G}^{WGAN-GP}=L_{G}^{WGAN} \\ \hat{x} = \alpha x + (1-\alpha) \tilde{x}$$ |
|      **DRAGAN**       | $L_{D}^{DRAGAN}=L_{D}^{GAN} + \lambda {\mathbb{E}}_{\tilde{x} \sim p_r+\mathcal{N}(0, c)}\left[\left(\left\|\nabla_{\hat{x}} D(\tilde{x})\right\|_{2}-1\right)^{2}\right] \\ L_{G}^{DRAGAN}=L_{G}^{GAN}$ |
|         hinge         | $\mathbb{E}[\max(0, 1-D(x))] + \mathbb{E}[\max(0, 1+D(G(z)))]\\-\mathbb{E}[D(G(x))]$ |
|                       |                                                              |

> inspired by [hwalsuklee](https://github.com/hwalsuklee/tensorflow-generative-model-collections)



本文主要要解释的是关于上述公式的一些变种，为了不被迷惑





接下来的详细展开，仅以Vanilla Loss举例，标准的Loss function是：
$$
\min_G \max_D \mathbb{E}_{x \sim p(x)}\left[\log D(x)\right] + \mathbb{E}_{z \sim p(z)}\left[\log \left(1 - D(G(z))\right)\right]
$$
具体展开写成两步分别优化应该是

优化判别器
$$
\max_D  \mathbb{E}_{x \sim p(x)}\left[\log D(x)\right] + \mathbb{E}_{z \sim p(z)}\left[\log \left(1 - D(G(z))\right)\right]
$$
优化生成器
$$

$$


---

而有时候我们能看到有些论文中的写法是：
$$
\begin{aligned}
L_D = E[f_D(-D(x))] + E[f_D(D(G(z))]
\end{aligned}
$$
这个写法最早出现在论文 Gradient descent GAN optimization is locally stable 中

Which Training Methods for GANs do actually Converge? 里也出现了



但他们其实是一致的

我们来看一下对 sigmoid 做对数操作会得到什么结果：
$$
\log \frac{1}{1+e^{-x}} = - \log(1 + e^{-x})
$$
所以这样你看两种写法是不是就完全一致了，因为 $D_1 = \text{Sigmoid}(D_2)$，是经过 Sigmoid 的输出值
$$
L_1 = - \log D_1(x) = \log(1 + e^{-D_2(x)})\\ 
f = \log(1+e^x), \quad L_2 = f\left(-D_2(x)\right) = \log(1+e^{-D_2(x)})
$$


如果是按这种写法，那我们可以统一成

non-saturating
$$
f_D(x) = f_G(x) = \log(1+e^x)
$$
hinge loss
$$
f_D(x) = \max(0, 1+x), \quad f_G(x) = x
$$

$$
\begin{aligned}
& \mathcal{L}(\theta, \phi)=\mathbf{E}_{\mathbf{z} \sim p_z, \xi \sim p_{\xi}}\left[f\left(D_{\theta_D}\left(G_{\theta_G}(\mathbf{z}, \xi)\right)\right)\right] \\
&+ \mathbf{E}_{I \sim p_{\mathcal{D}}}\left[f\left(-D_{\theta_D}(I)\right)+\lambda\left|\nabla D_{\theta_D}(I)\right|^2\right], \\
& \text { where } \quad f(u)=-\log (1+\exp (-u))
\end{aligned}
$$





