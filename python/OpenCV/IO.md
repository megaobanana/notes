`读取`图片(不能有中文路径)：

```python
import cv2 as cv
pic =cv.imread(路径带文件名和后缀,模式)  # 返回三维或二维(灰度)ndarray对象
```

| 模式为1                | 模式为0                     | 模式为-1                             |
| ---------------------- | --------------------------- | ------------------------------------ |
| 加载BGR通道，三维 数组 | 以灰度图模式读取，二维 数组 | 加载BGR+alpha(透明度)通道，三维 数组 |

`读取`图片(可以有中文路径，但要依赖matplotlib)：

```python
import cv2 as cv
import matplotlib.pyplot as plt
pic_rgb = plt.imread(路径带文件名和后缀) # matplotlib读出的图像为RGB，故需要转换一下，变成BGR
pic = cv.cvtColor(pic_rgb, cv.COLOR_BGR2RGB)
```

`写入`图片(不能有中文路径)：

```python
import cv2 as cv
cv.imwrite(路径带文件名和后缀,ndarray图片)
```

`写入`图片(可以有中文路径)：

```python
import cv2 as cv
cv.imencode(输出文件类型，注意不是真实后缀，只是代表导出类型，可选".jpg"或".png", ndarray图像)[1].tofile(路径带文件名和后缀)  # 使用分开
```

-
