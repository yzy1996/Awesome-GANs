StyleGAN1存在水滴问题，不仅图片中有，而且 feature map中也有

最后发现是AdaIN层导致的问题，因为IN是per-channel的，层与层之间的关系没有考虑

同时，作者注意到，std control 其实就是将feature map (per channel) 进行了一个放缩而已。这个操作可以被放到卷积层里，具体表现就是给卷积核乘以这些放缩参数（在paper中被称为weight demodulation）。





网络的层



