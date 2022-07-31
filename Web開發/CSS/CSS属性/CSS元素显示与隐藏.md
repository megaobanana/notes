## display: 

display除了能写inline/block/inline-block，当值为none的时候就能起到隐藏元素的作用

<font color=red>display隐藏元素后，**不再**占用原来的位置</font>



## visibility:

取值 inherit | visible | hidden

设置为hidden后保留原先的位置



## overflow:

<img align=left src="assets/image-20220712091443782.png" alt="image-20220712091443782" style="zoom:50%;" />

比如上面的文字，盒子太小，字太多，造成溢出

overflow:visible 不剪切内容也不添加滚动条

overflow:hidden能将溢出的部分隐藏起来

scroll:添加滚动条 

overflow-x: hidden --?

``
