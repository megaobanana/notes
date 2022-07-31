# 方法1：apt包管理系统安装

## 傻瓜操作

```bash
sudo apt install libopencv-dev
```



## 1.下载安装包、编译安装

(https://opencv.org/releases/)

wget https://github.com/opencv/opencv/archive/4.5.5.zip

（不知道为什么源码目录不能放在home目录中，得是home下的随便什么目录中，不然会导致安装错误，cuda下载时的deb包也不能放在home中）

解压后进入目录
下面的贡献库可下载可不下载
mkdir build（在源码文件夹opencv-x.x.x新建）
（sudo apt install cmake）
然后进入该目录（cmake会去当前目录的上一级找CMakelists，因此要先cd进来）

sudo cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_GENERATE_PKGCONFIG=ON ..
sudo make -j8
sudo make install



## 2.配置

sudo vim /etc/ld.so.conf

具体应该是要在这个文件里添加一行
include /usr/local/lib
然后运行sudo ldconfig（作用类似于刷新一下库的搜索路径的缓存，如果没做，可能会找不到刚安装的库）

------

sudo vim /etc/bash.bashrc

在文件末尾加入，添加如下内容后

```bash
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
export PKG_CONFIG_PATH
```

source /etc/bash.bashrc刷新shell的环境



## 3.验证安装

pkg-config opencv4 --modversion



## x.卸载

首先得cd到刚才建立的build目录

sudo make uninstall

然后把这个build目录也删掉

卸载系统自带的：sudo apt-get autoremove libopencv-dev