## 合上笔记本待机后就打不开了，只能强制重启

#### 1.检查是否安装了grep laptop-mode-tools 工具包

$ dpkg -l | grep laptop-mode-tools

如果执行命令无结果输出，表示未安装(如果已安装，忽略第2步)

#### 2.安装laptop-mode

执行命令：$ sudo apt-get install laptop-mode-tools

#### 3.判断Laptop是否启用了laptop_mode模式

cat /proc/sys/vm/laptop_mode

如果显示结果为0，则表示未启动，如果为非0的数字则表示启动了

#### 4.启动laptop-mode

修改配置文件/etc/default/acpi-support，更改 ENABLE_LAPTOP_MODE=true

直接在终端中输入 sudo laptop_mode start 启动了laptop_mode之后，在ubuntu挂起后，基本上就不会遇到无法唤醒的情况了

注：有些用户在acpi-support中并未找到 ENABLE_LAPTOP_MODE=true 被注释的项.看文件最后一行的提示

![img](https://upload-images.jianshu.io/upload_images/2006017-bccc6aa3cd5c319b.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/612/format/webp)

提示我们在/etc/laptop-mode/laptop-mode.conf 中进行配置

找到次文件查找 ENABLE_LAPTOP_MODE_ON_BATTERY、ENABLE_LAPTOP_MODE_ON_AC、ENABLE_LAPTOP_MODE_WHEN_LID_CLOSED

看注释大体明白什么意思 当用电池,外接电源,合上显示屏的时候是否启用 LAPTOP_MODE

全部设置为 1 就可以了。
