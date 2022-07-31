## 圆角

border-radius: ?px，(椭圆)圆与边框交集形成的圆角效果，或者也可以分别写四个

border-radius: ?px ?px ?px ?px;分别对应左上、右上、右下、左下

如果想要画一个圆

就新建一个盒子，宽高设置为相同的，然后border-radius=50%，半径等于宽的一半，不久正好是个圆吗



## 盒子阴影

```css
box-shadow: h-shadow v-shadow blur spread color inset;
```

| 值       | 含义                     |
| -------- | ------------------------ |
| h-shadow | 水平阴影的位置           |
| v-shadow | 垂直阴影的位置           |
| blur     | 模糊半径                 |
| spread   | 阴影尺寸                 |
| color    | 阴影颜色                 |
| inset    | inset/outset内部外部阴影 |



## 文字阴影

```css
text-shadow: h-shadow v-shadow blur color
```

| 值       | 含义           |
| -------- | -------------- |
| h-shadow | 水平阴影的位置 |
| v-shadow | 垂直阴影的位置 |
| blur     | 模糊半径       |
| color    | 阴影颜色       |