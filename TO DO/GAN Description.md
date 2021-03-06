



GAN learns to model a rich set of semantic and physical rules about the target distribution



我们在描述生成的数据时，可以用 generated samples\synthetic samples



Generative adversarial networks (GANs) offer a distinct and promising approach that focuses on a game-theoretic formulation for training an image synthesis model (Goodfellow et al., 2014).





produce convincing image samples on datasets with low variability and low resolution (Denton et al., 2015; Radford et al., 2015).





“Generative” because they output things like images rather than predictions about input (like “hotdog or not”); “adversarial networks” because they use two neural networks competing with each other in a “[cat-and-mouse game](https://www.nytimes.com/interactive/2018/01/02/technology/ai-generated-photos.html)”, like a cashier and a counterfeiter: one trying to fool the other into thinking it can generate real examples, the other trying to distinguish real from fake.



it’s a 0和游戏



Unlike other deep learning neural network models that are trained with a loss function until convergence, a GAN generator model is trained using a second model called a discriminator that learns to classify images as real or generated. Both the generator and discriminator model are trained together to maintain an equilibrium.



Generative models can be classified into two broad categories of explicit and implicit approaches. The former class assumes access to the model likelihood function, whereas the latter uses a sampling mechanism to generate data. Examples of explicit models are variational auto-encoders (VAEs) [19, 20] and PixelCNN [21]. Examples of implicit generative models are GANs. Explicit models are typically trained by maximizing the likelihood or its lower bound. GANs aim to approximate a data distribution P, using a parameterized model distribution Q. They achieve this by jointly optimizing two adversarial networks: a generator and a discriminator. The generator G is trained to synthesize from a noise vector an image that is close to the true data distribution. The discriminator D is optimized to accurately distinguish between the synthesized images coming from the generator and the real images from the data distribution. GANs have shown a dramatic ability to generate realistic high resolution images.





The software uses a generative adversarial network (GAN) approach, in which two neural networks play a game of cat and mouse, one attempting to generate artificial images indistinguishable from real photographs, the other attempting to tell the difference. The two networks train one another; after a few weeks, the image-creating network can produce images like the fakes on this website.



意义

GAN is the most interesting idea in the last 10 years in ML -Yann LeCun



It seems like a rather technical issue, but I really think it opens the door to an entire world of possibilities.

打开新的大门

表征



**Application**

They are used widely in image generation, video generation and voice generation.



生成了假的干什么呢

2018 10 25 一副GAN生成的画在佳士得拍卖行卖出了

put the first AI portrait in Christie’s

[Christie’s sold a portrait](https://www.theverge.com/2018/10/23/18013190/ai-art-portrait-auction-christies-belamy-obvious-robbie-barrat-gans) for $432,000 that had been generated by a GAN



为什么要随机噪声

因为G学习的是从一个分布到另一个分布的映射 z->data manifold

G也掌握了图片的特征，而且是图片本质的特征





So discriminative algorithms map features to labels

generative algorithms attempt to predict features given a certain label. Assuming this email is spam, how likely are these features? 

While discriminative models care about the relation between `y` and `x`, generative models care about “how you get x.” They allow you to capture `p(x|y)`,



That said, generative algorithms can also be used as classifiers. It just so happens that they can do more than categorize input data.



Discriminative models learn the boundary between classes

Generative models model the distribution of individual classes







They consist of hundreds and thousands of labeled data. In other words, these collections are composed of *(x,y)* pairs where (x) is the raw data, an image matrix for instance, and (y) is a description of what that data point (x) represents.





This kind of situation could be modeled as a minimax game in Game Theory. And this process is called Adversarial Process.





GAN [9] can generate samples similar to a data distribution through a two-player game between a generator G and a discriminator D.







It is proved in [9] that this minimax game has a global optimum when the distribution pg of the synthetic samples and the distribution pd of the training samples are the same. Under mild conditions (e.g., G and D have enough capacity), pg converges to pd. In practice, it is better for G to maximize log(D(G(z))) instead of minimizing log (1 − D(G(z))) [9].



The goal of the generative model is to learn the underlying probabilistic distribution of unlabeled data by disentangling explanatory factors in the data [ Learning deep architectures for ai, e. A note on the evaluation of generative models]



### 写在Related work里的

**GAN:**

The GAN[^1] has two networks: a generator G that tries to generate real data given noise $z \sim p_z(z)$, and a discriminator $D \in [0, 1]$ that classifies the real data $x \sim p_{data}(x)$ and the fake data G(z). The D(x) represents probability of x being a real data. The objective of G is to fit the true data distribution deceiving D by playing the following minimax game:





Generative Adversarial Network (GAN) consists of a generator G and a discriminator D that compete in a twoplayer minimax game. D tries to distinguish a real image x from a synthetic one G(z), and G tries to synthesize realistic-looking images that can fool D. Concretely, D and G play the game with a value function V (D,G): 




$$
\min _{\theta_{G}} \max _{\theta_{D}} \mathbb{E}_{x \sim p_{\text {data}}(x)}[\log D(x)]+\mathbb{E}_{z \sim p_{z}(z)}[\log (1-D(G(z)))]
$$
where $\theta_G$ and $\theta_D$ are parameters of G and D, respectively.



被证明收敛性

It is proved in [^1] that this minimax game has a global optimum when the distribution $p_g$ of the synthetic samples and the distribution $p_d$ of the training samples are the same. Under mild conditions (e.g., G and D have enough capacity), $p_g$ converges to $p_d$.





**CGAN:**

The objective of conditioned GANs is to fit conditional probability distribution $p(x|c)$ where c is condition that describes x. The objective is to learn $p(x|c)$ correctly from a labeled dataset $(x_1, c_1),(x_2, c_2), ...,(x_n, c_n)$. The generator G(z, c) of conditioned GAN has additional input c, and all generators used in our experiment take [x, c] as an input where [...] means vector concatenation. We can add c into the input of D(x, c) as well, or put regularization terms to guide the generator. If we use D(x, c), then the objective of the conditioned GAN is to optimize the equation 1 for each c:
$$
\min _{\theta_{G}} \max _{\theta_{D}} \mathbb{E}_{c \sim p_{\text {data}}(c)}\left[\mathbb{E}_{x \sim p_{\text {data}}(x \mid c)}[\log D(x, c)]+\mathbb{E}_{z \sim p_{z}(z)}[\log (1-D(G(z, c), c))]\right]
$$
where D(x, c) represents probability of x being a real data from condition c.



**SGAN:**

Springenberg [35] generalizes GAN to learn a discriminative classifier where D is trained to not only distinguish between real and fake images, but also classify real images into K classes. D outputs a (K+1)-dim vector with the last dimension for the real/fake decision. The trained D is used for image classification. DR-GAN shares a similar loss for D as [35] but has two additions.First, we expand G with an encoder-decoder structure. Second, we have an additional side information classification on the pose while training D.





### 写在摘要里的

应用的价值，列举案例和论文

The GAN [^1] is a prominent generative model that is found to be useful for unsupervised learning [^2], semi-supervised learning[^3], super resolution[^4], text-to-image[^5], and image inpainting[^6]. 

证明可收敛

The potentiality of GAN was supported by the theory that if the model has enough capacity, the learned distribution can converge to the distribution over real data[^1]. 

一些提高GAN效果的方法，稳定性和多样性

The representative power of the GAN was highly enhanced with deep learning techniques[^2] and various methods[^7][^8] was introduced to stabilize the learning process.



[^1]: Generative adversarial nets
[^2]: Unsupervised representation learning with deep convolutional generative adversarial networks
[^3]: Semi-Supervised Learning with Generative Adversarial Networks
[^4]: Photo-realistic single image super-resolution using a generative adversarial network
[^5]: Generative adversarial text to image synthesis
[^6]: Context encoders: Feature learning by inpainting
[^7]: Improved techniques for training gans
[^8]: Energy-based generative adversarial network

