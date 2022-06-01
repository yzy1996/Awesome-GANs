GAN models share two common aspects: solving a challenging saddle point optimization problem, interpreted as an adversarial game between a generator and a discriminator functions.

a popular paradigm to learn the distribution of the observed data



Generative models aim to approximate samples from a complex high-dimensional target distribution $\mathbb{P}$. 

The adversarial mechanism reflects by a generator and a discriminator who compete against each other. Unlike other deep neural network models trained with a loss function until convergence, GAN train these two together to maintain a equilibrium finally.

The generator learns to map from a low-dimension space $\mathcal{Z}$ to a high-dimension space $\mathcal{X}$ with a model distribution $\mathbb{Q}$.

The discriminator learns to accurately distinguish between the synthesized data $\mathbf{Y}$ coming from $\mathbb{Q}$ and the real data $\mathbf{X}$ from $\mathbb{P}$. 

We can denote by $\mathbb{P}$ and $\mathbb{Q}$ the data and model distribution, respectively.



Generative Adversarial Network (GAN) is formulated as a two-player game between a gnerator (G) and a discriminator (D), where G targets at reproducing the distribution of observed data through synthesising new samples, and D competes with G by distinguishing the generated images from the real ones. In priciple, they are expected to reach an equilibrium where D cannot tell the real and fake images apart.



GAN use the reparametrization trick to sample from a complex probability distribution by learning a transformation $y=f(x), x\sim N(0, I)$, where f is the transformatioin function modelled by a neural network.



integral probability metrics (IPMs)

> a “well behaved” function with large amplitude where $P_x$ and$P_z$ differ most

- Wasserstein IPMs



Maximum Mean Discrepancies (MMDs)

> the critic function is a member of a reproducing kernel Hilbert space

### objective functions of GANs



**vanilla GAN**
$$
\min _{G} \max _{D} V(D, G)=\mathbb{E}_{\boldsymbol{x} \sim p_{\mathrm{data}}(\boldsymbol{x})}[\log D(\boldsymbol{x})]+\mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z})))]
$$

$$
\min J^G = \mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z})))]
$$

where $J^G$ is the cost of for generator, $\log D(x)$ is the cross-entropy between $[D(x) \quad 1-D(x)]^T$ and $[1 \quad 0]^T$. Likewise,  $\log (1-D(G(z)))$ is the cross-entropy between $[1-D(G(z)) \quad D(G(z))]^T$ and $[1 \quad 0]^T$. It’s because that the cross-entropy 

For a fixed generator $G$, the optimal discriminator $D$ is:
$$
D^*(x)=\frac{p_{data}(x)}{p_{data}(x)+p_{g}(x)},
$$
For this optimal $D^*$, the optimal $G$ satisfies:
$$
p_g(x) =p_{data}(x).
$$

> Problem: 
>
> The cross-entropy of $G$ can be expressed as follow:
> $$
> H^G = 1 * \log(1-D(G(z))) + 0*log(D(G(z))) = \log(1-D(G(z)))
> $$
> In early training progress, D can easily distinguish fake samples from real samples ($D(G(z)) \rightarrow 0$). This results in G not having sufficient gradient to improve, which is called **training instability**. Rather than training G in the way of Equation (2), another way of Equation (6) could provides larger gradients in early training.
> $$
> \min J^G = \mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[-\log (D(G(\boldsymbol{z})))]
> $$
> So a new cross-entropy of $G$ can be expressed as:
> $$
> H = 1 * \log(-D(G(z))) + 0*log(1 + D(G(z)))
> $$



blog 

https://www.freecodecamp.org/news/an-intuitive-introduction-to-generative-adversarial-networks-gans-7a2264a81394/

https://wiki.pathmind.com/generative-adversarial-network-gan









A GAN consists of a generator $G$ and a discriminator $D$, both are conducted by a neural network. $G$ takes a latent variable $z \sim p(z)$ sampled from a prior distribution and maps it to the observation space $\mathcal{X}$. $D$ takes an observation $x \in \mathcal{X}$ and produces a decision output over possible observation sources (either from $G$ or from the empirical data distribution). 



The generator and the discriminator in the standard GAN training procedure are trained by minimizing the following objectives:
$$
\begin{align}
&L_{D}=-\mathbb{E}_{x \sim p_{\text {data }}}[\log D(x)]-\mathbb{E}_{z \sim p(z)}[1-\log D(G(z))], \\
&L_{G}=-\mathbb{E}_{z \sim p(z)}[\log D(G(z))].
\end{align}
$$
This formulation is originally proposed by Goodfellow et al. (2014) as non-saturating (NS) GAN. A significant amount of research has been done on modifying this formulation in order to improve the training process. A notable example is the **hinge-loss** version of the adversarial loss:
$$
\begin{align}
&L_{D}=-\mathbb{E}_{x \sim p_{\text {data }}}[\min (0,-1+D(x))]-\mathbb{E}_{z \sim p(z)}[\min (0,-1-D(G(z)))], \\
&L_{G}=-\mathbb{E}_{z \sim p(z)}[D(G(z))].
\end{align}
$$
Another commonly adopted GAN formulation is the **Wassertein** GAN (WGAN), where the authors propose clipping the weights to enforce the continuous of Wassertein distance. The loss function of WGAN is:
$$
\begin{align}
&L_{D}=-\mathbb{E}_{x \sim p_{\text {data }}}[D(x)]+\mathbb{E}_{z \sim p(z)}[D(G(z))], \\
&L_{G}=-\mathbb{E}_{z \sim p(z)}[D(G(z))].
\end{align}
$$



[How to Train a GAN? Tips and tricks to make GANs work](https://github.com/soumith/ganhacks)











