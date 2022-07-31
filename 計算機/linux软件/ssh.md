## 安装

sudo apt-get install openssh-server



## 验证安装

pi@LEGION:~$ sudo ps -e | grep ssh

应该出现下列类似内容

  26076 ?        00:00:00 sshd

## 启动（默认应该是自动启动的）

sudo service ssh start