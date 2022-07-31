![image-20220530194355122](assets/image-20220530194355122.png)-

- workspace：工作区，就是在电脑里平时访问使用的那个目录
- staging area：暂存区/缓存区，处于workspace中的隐藏文件夹.git中的index文件里
- local repository：版本库或本地仓库，暂存区/缓存区，处于workspace中的隐藏文件夹.git中
- remote repository：远程仓库，在别的电脑上



## 安装

```bash
# 安装git
apt install git
# 设置git关联的文字编辑器
git config --global core.editor vim
```



## git init

使用此指令来将当前目录作为 Git 仓库，使用完此指令后，当前目录下会多出来一个隐藏目录.git，里面就是仓库的内容，以及缓存文件index



## git add

此命令将要提交的文件的信息添加到索引库中(将修改添加到暂存区)，以准备为下一次提交分段的内容。 它通常将现有路径的当前内容作为一个整体添加，但是通过一些选项，它也可以用于添加内容，只对所应用的工作树文件进行一些更改，或删除工作树中不存在的路径了。

“索引”保存工作树内容的快照，并且将该快照作为下一个提交的内容。 因此，在对工作树进行任何更改之后，并且在运行`git commit`命令之前，必须使用`git add`命令将任何新的或修改的文件添加到索引。

该命令可以在提交之前多次执行。它只在运行`git add`命令时添加指定文件的内容; 如果希望随后的更改包含在下一个提交中，那么必须再次运行`git add`将新的内容添加到索引。

```bash
$ git add .  # 将所有修改添加到暂存区
$ git add *Controller   # 将以Controller结尾的文件的所有修改添加到暂存区
$ git add Hello*   # 将所有以Hello开头的文件的修改添加到暂存区 例如:HelloWorld.txt,Hello.java,HelloGit.txt ...
$ git add Hello?   # 将以Hello开头后面只有一位的文件的修改提交到暂存区 例如:Hello1.txt,HelloA.java 如果是HelloGit.txt或者Hello.java是不会被添加
```



## git commit

提交到仓库，这时会使用默认文字编辑器打开一份生成的文档，里面展示了这次add了的全部内容。不过这些内容由于是给你看的，让你了解一下差异，所以全部用 # 注释掉了，你要做的，就是写上一行没有被注释掉的话，内容就是这次做了什么改动啊blahblahblah，好让别人知道这次commit的版本有什么人为总结的变动，而不是看到机器总结的一堆难以阅读的变动信息。

或不检查修改内容，直接写提交注释`git commit -m "提交信息"`




## 提交到远程仓库

如果按刚才的流程已经init了本地仓库，然后commit了

上传到云只需要用以下语句

```bash
git remote add origin https://gitee.com/megaobanana/PROJECT-GPBI.git
git push -u origin "master"
```

origin就是你为远端仓库所起的名字，其实你也可以要Ceres 或者Earth，后面就是仓库网址

下次提交就不需要再remote add了

### 换仓库：

如果SSL证书验证错误：git config --global http.sslVerify “false”

1.先把原来的仓库删了`git remote remove origin`

2.然后可以查看下是否删了`git remote -v`

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

## 从远程仓库下载

```
git clone https://gitee.com/megaobanana/PROJECT-GPBI.git
```

下载完如果做了一些改动，可以add,commit后直接git push到远程服务器，不用再像刚才一样配置了

git clone是在本地啥也没有的情况下想要获取一份仓库副本时使用的指令

如果本地已经有仓库了，只是想同步一下，需使用使用

```
git pull
```

这个指令会同时更新本地仓库.git和工作区

如果只想更新仓库，确认一下更新的内容，需要先`git fetch`再`git merge`



## git checkout/branch

从已有的分支创建新的分支(如从master分支),创建一个dev分支

```bash
git checkout -b dev//基于本地创建分支
git checkout -b dev origin/dev //基于远程分支创建本地分支

可以看到git checkout -b命令相当于
创建分支： git branch dev
切换分支： git checkout dev

删除本地分支
git branch -D dev
删除远程分支
git push origin :branch-name

```



## tag
