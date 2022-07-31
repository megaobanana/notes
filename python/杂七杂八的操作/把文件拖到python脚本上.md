默认情况下，我们无法拖放一个文件给python脚本让其去处理这个文件，这是因为windows认为python脚本不是一个合法的`可拖放的目的对象`（drop target）。为了实现拖放目的，我们还得修改注册表来修改对象类型。但是bat脚本是`可拖放的目的对象`，所以用bat脚本配合python的方式会更加简单

------

将文件拖拽到我上.bat

```bash
:: 写上这条指令，不然执行bat时会把下列的每条指令都打在公屏上
@echo off
:: %*代表的是拖拽到bat脚本上的所有文件的集合，最好把这个值保存在变量里，不然待会调用函数的时候再使用%*好像值就不一样了？
set dragged_items=%*
:: %0代表的是该文件本身所在的地址，如C:\Users\CSD\Documents\Enote_database\__batch_processor__\将文件啥啥啥.bat
set LocalPath=%0
:: 这是在调用下面那个execute_python_script函数，参数就为刚才设置的LocalPath
call :execute_python_script %LocalPath%
:: 显示一行“按下任意按钮以继续...”
pause


:execute_python_script
:: 下面的等号后边写同级目录中那个python脚本的名称
set python_script=mainscript.py
:: 这是把刚才批处理脚本自身的 文件地址 中的自身名称（将文件啥啥啥.bat）给删掉了，剩下一个路径，然后把python脚本的路径跟它的路径拼接起来，就变成python脚本的路径了
:: （当然前提肯定就是你得把python脚本和bat脚本放在一个目录下啦=_=）
set file_path=%~dp1%python_script%
:: 最后，终于可以执行python脚本了，参数就是刚才拖拽到bat上的那些文件
python %file_path% %dragged_items%
```

mainscript.py

```python
import sys

file_paths = sys.argv[1:]  # 去掉第一个是因为第一个参数就本python脚本的名称，没有意义
for i in file_paths:
    print(i)
```

