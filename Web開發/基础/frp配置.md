## 客户端配置（就是用户最终想连接到的设备）

https://github.com/fatedier/frp/tree/master

下载玩后修改frpc.ini，运行配置参数都在这里面

------

[common]
**server_addr = frp.freefrp.net**
服务提供商提供的 frp 服务器 IP 地址或者域名地址 
**server_port = 7000**
服务提供商提供的 frp 服务端口号 （具体来说是服务器端frps.ini中[common]项的bind_port值）
**token = freefrp.net**
服务提供商提供的密码 

如下：

```ini
[common]
server_addr = frp.freefrp.net
server_port = 7000
token = freefrp.net
```

```ini
[common]
server_addr=39.99.224.141
server_port=2333
```

------

如果客户端想用ssh链接这台服务器，则需添加如下字段（当然下列参数配置成功后其实不仅可以用来连ssh，传输任意数据都可以，比如说运行socket测试程序之类的）

**[yourname_linux_ssh]**
服务名称 : **重点参数**,此处为该条穿透服务的名称,必须修改,且不能与其他用户重复.为保证唯一性,建议以类似示例中 [yourname_linux_ssh] 的方式命名.**此条记录重复会导致 frp 客户端无法启动.**
**type = tcp** 
协议类型 : 确保本条穿透服务使用此协议能够在内网正常使用或访问.例如,尝试在本地终端执行 ssh root@192.168.1.5 确保能够正常登录. 
**local_ip = 192.168.1.4** 
内网 IP : 本地服务所在设备的内网 IP 地址.由于 frp 客户端有可能安装在 docker 容器中,所以请不要使用 127.0.0.1 来表示本机 IP. 
**local_port = 22**
本地端口 : 本地服务的端口号.例如,本地 linux 服务器的默认 SSH 登录端口为 22. 
远程端口 : 远程服务的端口号.自定义填写一个远程服务端口号,例如 22222 ,成功连接后,可以使用 ssh -p 22222 root@frp.freefrp.net 来远程登录你的内网 Linux 服务器.**远程端口号必须根据服务提供商提供的服务端口范围进行自选填写,确保不要与其他用户重复,如果访问的内容不是自己的服务,则表示该端口号已被其他用户使用.此条记录重复或者超出端口号范围会导致无法连接或者 frp 客户端无法启动.**

如下：

```ini
[OuYangWuShuang_linux_ssh]
type = tcp
local_ip = 192.168.1.6
local_port = 22
remote_port = 48537
```

------

运行：

sudo chmod +x ./frpc

./frpc
