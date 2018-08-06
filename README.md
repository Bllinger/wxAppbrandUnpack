### 解压微信小程序包（.wxapkg）的工具<br>
usage：unwxpack.py _411754859_5.wxapkg<br>
两个参数，第二个为微信小程序包源文件路径<br>
解压结果没完全还原，若想还原为编译前的内容，推荐一下这篇文章https://bbs.pediy.com/thread-225289.htm<br>
下面这图为微信小程序的文件格式，first_mark和last_mark两个的类型应该为Uchar，图中给错了<br>
 ![image](https://github.com/Bllinger/wxAppbrandUnpack/blob/master/format.png)
