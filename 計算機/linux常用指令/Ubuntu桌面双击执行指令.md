新建xxxx.desktop

```
[Desktop Entry]
Name=Eject /dev/sda
Exec=udisksctl power-off -b /dev/sda
Terminal=true
Type=Application
```

<img src="assets/image-20220514135858855.png" alt="image-20220514135858855" style="zoom:80%;" />

注意这个文件名不会显示在桌面上，实际上显示的文件名是Name=后面的东西，比较特别

Exec=后面是要执行的指令

另外编辑完了以后，要加上执行权限，这还不够，还要右键——Allow launching（不在properties里，是右键后单独的一个选项）