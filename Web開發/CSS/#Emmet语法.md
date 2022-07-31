Emmet语法的前身是Zen coding，它使用缩写来提高html/css的编写速度，VScode内部已经集成该语法

## Emmet生成HTML标签：

1. 生成标签，直接输入标签名再按tab即可，比如div然后按tab，就可以生成\<div>\</div>

2. 如果要生成包含==父子==关系的标签，可以用 \> 比如 ul>li (无空格)再按tab就生成一对\<li>包含在一对\<ul>中

3. 如果要生成包含==并列==关系的标签，可以用 + ，如 div+p

4. 如果想要给标签快捷添加==所属类或id==，可用 标签名.类名 、标签名#id名

   如 写`p.one`再按tab会生成 `<p class="one"></p>`



还有一些特殊符号，如

1. \*号，会把*号前面的任意标签复制这么多次

   如：`div*5`+tab会生成5个并列的`<div></div>`

   `ul>li*5`+tab会生成一个`<ul></ul>`，其中包含五个`<li></li>`

2. \$号，本身会被看做是一个字符，具体位置放在哪都行，在与\*号配合使用的时候，其值会在副本中被依次填入1,2,3,4,5...

   如：`p.demo*5`+tab会生成如下内容

   ```css
   <p class="demo1"></p>
   <p class="demo2"></p>
   <p class="demo3"></p>
   <p class="demo4"></p>
   <p class="demo5"></p>
   ```

3. {}号，跟在标签后面，表示这个标签会添加大括号中的内容，大括号内也可包含`$`以替换数字

   `ul>li{hello$$}*5`+tab会生成如下

   ```css
   <ul>
       <li>hello01</li>
       <li>hello02</li>
       <li>hello03</li>
       <li>hello04</li>
       <li>hello05</li>
   </ul>
   ```



## Emmet生成CSS：

采用首字母缩写即可

`tdn`+tab-->`text-decoration: none;`

`tac`+tab-->`text-align: center;`

`ti2em`+tab-->`text-indent: 2em;`
