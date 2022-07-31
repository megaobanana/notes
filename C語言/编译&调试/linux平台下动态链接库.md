可以使用ldd命令来确定某一程序是否是静态链接的：
```bash
ldd [程序名称]
```
如果是动态的，此指令还会列出所需要的动态库
在linux平台上，动态装入器负责装入动态链接的可执行程序运行所需的动态库
而动态装入器找到共享库需要依赖两个文件：
`/etc/ld.so.conf`和`/etc/ld.so.cache`
ld.so.conf中是动态链接库的搜索清单但除去了/lib和/ usr/lib，因为这两个是默认的最基本的搜索目录

> 但是如果刚修改完ld.so.conf，动态装入器也不会搜索到新加入的目录，因为它读取的是/etc/ld.so.cache
> 需要使用ldconfig命令来将/etc/ld.so.conf内数据读入缓存

------

一般通过源码包安装程序时，会分为以下三个步骤:
configure，make和make install
其中make的阶段可能有的教程说要加一个-prefix=xxx
如果一个这个安装的程序能 **提供一些动态库** ，则在源码中肯定有一个或多个.pc文件，.pc文件中包含了库的版本信息，作者，信息等等
当执行完make install后这些.pc文件会被复制到${prefix}/lib/pkgconfig里，这个prefix就是刚才写的目录
当然，安装一个软件也会依赖一些动态库，是否有符合版本的库？这些库在哪里？make大多数情况下会依赖依赖pkg-config这个工具来找，而pkg-config寻找的就是先去PKG_CONFIG_PATH，再去预设目录中的.pc文件

------

但是pkg-config又要去哪里找安装路径呢？

要通过BASH寻找环境变量，因此具体的设置方法为
```bash
sudo gedit /etc/bash.bashrc  #不一定是gedit，什么vim啊nano啊是个文字编辑器就行，每一个运行bash shell的用户都会执行此脚本
############
在文件末尾加入
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/xxx/xxx/xxx.../pkgconfig
export PKG_CONFIG_PATH
保存并退出
############
source /etc/bash
```

------

总之：

pkg-config的相关配置决定了软件==能不能安装上==
/etc/ld.so.conf设置正不正确决定了一个程序能不能真正运行起来

------

不过，在编译和动态库相关的程序时，可以使用-L [地址来指定动态库位置]，也可以使用`pkg-config --cflags --libs opencv4`，这时pkg-config发挥着根据.pc反馈所需库所f在地址的功能，这时pkg-config也决定着软件==能否成功编译==

有什么好处呢？

比如跟同事工作，大伙都装了一样的库，但是具体位置每个人选的都不一样，如果把编译时的位置定死了
同事A说我在我电脑上能编译，同事B就觉得奇怪，在我这怎么也过不了编译