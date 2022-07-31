### 1.下载安装包（准确地来说应该是自解压文件）

https://opencv.org/releases/或[查看笔记附带](./)

解压到这个目录☆

<div align=left><img src="assets/image-20220513200744622.png" alt="image-20220513200744622" style="zoom:50%;" /></div>

### 2.测试源码

```makefile
# make sure the extraction path of Opencv is C:\Program Files\OpenCV !

all:Run_me.exe

Run_me.exe:main.cpp
	g++ -g main.cpp -o Run_me.exe -I "C:\Program Files\OpenCV\opencv\build\include" -I "C:\Program Files\OpenCV\opencv\build\include\opencv2" -L "C:\Program Files\OpenCV\opencv\build\x64\vc15\lib"
```

```c++
#include <opencv2/opencv.hpp>

//#pragma comment(lib,"C:/Program Files/OpenCV/opencv/build/x64/vc15/lib/opencv_world455.lib")  // release模式编译时用这个
#pragma comment(lib,"C:/Program Files/OpenCV/opencv/build/x64/vc15/lib/opencv_world455d.lib")  // debug模式编译时用这个

using namespace cv;
int main()
{
    Mat image;
    image = imread("./test.jpg", 1 );
    namedWindow( "Display Image", WINDOW_AUTOSIZE);
    imshow( "Display Image", image );
    waitKey(0);

    return 0;
}
```

mingw32-make.exe编译