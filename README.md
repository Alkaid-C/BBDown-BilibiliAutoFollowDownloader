这是一个调用[BBDown](https://github.com/nilaoda/BBDown)自动下载关注列表中的UP主的新视频的Python脚本。仅适配Windows系统。

### 这个脚本试图解决什么问题

或许因为本人位于非中国大陆地区，在线播放B站4k视频时经常遭到卡顿。为避免卡顿，考虑下载后观看，因此找到了BBDown项目。但在看到感兴趣的视频后再手动下载，仍需等待一段时间。此脚本将自动下载关注列表中的UP主视频到本地，等到闲暇时直接打开本地文件夹即可挑选视频观看。

### 如何使用这个脚本

* 下载并安装Python。
* 下载BBDown项目的可执行文件，将其放置到**下属的BBDown文件夹内**，并根据该项目的文档配置BBDown。以下是个人关于如何配置BBDown的一些说明（针对1.60版本）：
  * 下载ffmpeg，并将其放置到**下属的BBDown文件夹内**。
  * 在命令行中打开BBDown，使用login指令登录。（按Win+R，输入cmd后回车 - 在弹出窗口中输入cd 【BBDown.exe所处的路径名称】，如cd D:\BBDown-BilibiliAutoFollowDownloader\BBDown\，回车- 输入 BBDown login，回车- 扫描二维码登录 - 关闭窗口）。
  * 使用文本编辑器在BBDown文件夹内新建文件BBDown.config，参照BBDown项目中的说明进行进一步配置。
* 在主目录的FollowList.txt中填入你想要追更的UP主的主页链接，（形如https://space.bilibili.com/869610/）每行一个。
* 点击BilibiliFollowAutoDownloader.py执行首次运行。首次运行将不会下载任何视频；只有首次运行后新上传的视频会被下载。
* 使用Task Scheduler/任务计划程序将此脚本设为定时运行（如每天一次），**注意将起始目录设为脚本目录**。详细说明如下：
  * 按Win+R，输入taskschd.msc后回车，打开Task Scheduler/任务计划程序。
  * 点击右侧“Create Basic Task/创建基本任务”。
  * 在弹出窗口中输入任务名称，点击下一步。
  * 设置Trigger/触发器，建议选择每日或当前用户登陆时，点击下一步。
  * 在Action/操作一栏选择“Start a program/启动程序”。
  * 在程序和脚本一栏点击浏览，找到BilibiliFollowAutoDownloader.py并点击打开。
  * **在“Start in/起始于”**一栏输入脚本所在的目录，如D:\BBDown-BilibiliAutoFollowDownloader\BBDown\。
  * 点击完成。
* 当你想要添加新的up主时，请在FollowList.txt第一行添加新up主的空间链接。
* 如试图从列表中删除up主，请清空BBDown\New_AV_List文件夹中的所有缓存文件，随后手动运行脚本一次。