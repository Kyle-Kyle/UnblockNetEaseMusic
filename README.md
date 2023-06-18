# 简介
一个简单的deploy-and-forget-able的脚本来帮助大家在海外正常使用网易云。

# 原理
每日自动用国内IP和网易云服务器交互一次来绕过IP限制。

# 使用方法

## 1. 准备需要的参数
本项目成功运行需要一个参数`MUSIC_U`.
- 打开网易云(https://music.163.com/) --> 按下`F12` --> `Application` --> `Cookies` --> `https://musci.163.com`
- 找到所需要参数对应的数据.

## 2. 运行docker
~~~
docker run -d -e MUSCI_U=<参数> jkjh1jkjh1/unblockneteasemusic
~~~
命令运行完，各平台上的IP限制应该就都消失了，可以听所有的歌了。
该docker image会每日定时(00:01 AM)自动完成交互，不需要重复部署。

# 参考项目
[NetEaseMusicWorldPlus](https://github.com/nondanee/NetEaseMusicWorldPlus)

# Acknowledgement
感谢网易云陪我度过每一个睡眼惺忪的早晨。
