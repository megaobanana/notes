字体：

```css
font-family: "Microsoft Yahei", Arial, Helvetica;
```

优先级从前到后，多个字体用逗号分隔，带空格的字体名字最好用引号包含

字号：

```css
font-size: ?px;
```

不同浏览器默认显示字号不一致，尽量给一个明确的大小

粗细：

```css
font-weight: bold/normal/数字;
```

颜色：

```css
color: 内置/rgba(?,?,?,?)/rgb(?,?,?)/#??????;
```

对齐：

```css
text-align: left/center/right;
```

划线：

```css
text-decoration: underline/overline/none/line-through;
```

缩进：

```css
text-indent: 20px/2em;
```

em是一个相对单位，就是当前元素（font-size）1个文字的大小

行间距：

```css
line-height: 26px;
```

文字居中：CSS没有直接给文字居中的代码，但是可以使用一个小技巧：让文字的行高等于父容器的高度

```
height: [数值]px;
line-height: [数值px];
```

