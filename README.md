# Arcane Style Transfer 

> 23Spring 重庆大学计算机学院 深度学习课程项目-任务6

<div align=center>
    <img src="./imgs/cover.png" style="zoom: 50%; " />
</div>

## 项目简介
双城之战主角金克斯有句台词是“我有最美好的初衷”奈何却总是好心办了“坏事”。而希尔科最初因为与范德尔选择了不同的道路而决裂了，但到最后的时候希尔科却越来越像范德尔。希尔科最后对金克斯说的“你，我什么都不换”更是让无数玩家泪崩。出于对双城之战画风的喜爱，本项目将利用生成对抗网络(GAN)实现双城之战动画进行风格迁移。

## 项目结构
```
├── README.md
├── scripts # 运行脚本
├── pytorch-CycleGAN-and-pix2pix # Pix2Pix
│   ├── datasets
│   ├── ...
├── UGATIT-pytorch # UGATIT
│   ├── datasets
│   ├── ...
├── utils # 评价指标
│   ├── FID.py
│   ├── LPIPS.py
├── metrics.py # 评价指标
```

## 运行
利用`Scripts`中的脚本进行快速运行

## 基础版-Pix2Pix
> !TODO

## 进阶版-UGATIT
> !TODO


## 评价指标
实验指标选取FID和LPIPS，FID用于衡量生成图像与真实图像的相似度，LPIPS用于衡量生成图像与风格图像的相似度。
### FID

### LPIPS

## 实验结果
### 实验参数

## 参考资料
1. Pix2Pix：《Image-to-image translation with conditional adversarial networks》
2. U-GAT-IT：《U-GAT-IT: UNSUPERVISED GENERATIVE ATTENTIONAL NETWORKS WITH ADAPTIVE LAYER- INSTANCE NORMALIZATION FOR IMAGE-TO-IMAGE
TRANSLATION》
3. Github Official Code：[pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
4. Github Official Code：[UGATIT](https://github.com/znxlwm/UGATIT-pytorch)