作为linux平台使用最为广泛的调试软件，自然有各种各样的安装方法，比如`sudo apt install gdb`

但想调试程序，仅仅有这个软件还是不够的，还要给编译器加上一个-g的选项

> 对于需要分布编译的程序，比如先输出.o，然后链接成.out。其中每一步都要加上-g(作为第一个参数)
>
> 比如g++ -g -c main.cpp
> g++ -g main.o -o main.out

启动调试器：

先cd到这个目录下：然后

`gdb main.out`

如果出现`reading symbools fromxxx`则表明成功以调试模式编译了

然后最后一行输出的是(gdb)，括号后面输入的就是各种各样的指令了

输入一个单l (link的l，可能显示不清楚)

则会显示源码，默认只显示10行，想要继续显示则按enter

| 调试指令                                               | 作用                                                         |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| `(gdb)  break xxx` or `(gdb) b xxx`                    | 在源代码指定的设置断点，其中  xxx 用于指定具体打断点的位置。 |
| `(gdb)  run` or` (gdb) r`                              | 执行被调试的程序，其会自动在第一个断点处暂停执行。           |
| `(gdb)  continue` or `(gdb) c`                         | 当程序在某一断点处停止运行后，使用该指令可以继续执行，直至遇到下一个断点或者程序结束。 |
| `(gdb)  next` or `(gdb) n`                             | 令程序一行代码一行代码的执行。                               |
| `(gdb)  print xxx` or `(gdb) p xxx`                    | 打印指定变量的值，其中  xxx 指的就是某一变量名。             |
| `(gdb)  list` or `(gdb) l`                             | 往后显示10行                                                 |
| `(gdb) list-` or  `(gdb) l -`                          | 往前显示10行                                                 |
| `(gdb) list[类名或函数名]` or `(gdb) l [类名或函数名]` |                                                              |
| `(gdb)ctrl+D`                                          | 退出程序                                                     |
| `(gdb)info b`                                          | 查看已有的断点                                               |
| `(gdb)clear xxx`                                       | 清除断点                                                     |

监视：

(gdb) watch *地址  # 当地址所指内容发送变化时断点

(gdb) watch var  #当var值变化时，断点

(gdb) watch (condition)  #当条件符合时，断点



#### vscode在linux下使用gdb来debug的.json文件

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
            {
                "name": "g++ - Build and debug active file",
                "type": "cppdbg",
                "request": "launch",
                "program": "${fileDirname}/${fileBasenameNoExtension}.out",
                "args": [],
                "stopAtEntry": false,
                "cwd": "${fileDirname}",
                "environment": [],
                "externalConsole": false,
                "MIMode": "gdb",
                "setupCommands": [
                    {
                        "description": "Enable pretty-printing for gdb",
                        "text": "-enable-pretty-printing",
                        "ignoreFailures": true
                    }
                ],
                "miDebuggerPath": "/usr/bin/gdb"
            
        }
    ]
}
```

