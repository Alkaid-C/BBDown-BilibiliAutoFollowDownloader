这是一个调用[BBDown](https://github.com/nilaoda/BBDown)自动下载关注列表中的UP主的新视频的Python脚本。仅适配Windows系统。

### 这个脚本试图解决什么问题

或许因为本人位于非中国大陆地区，在线播放B站4k视频时经常遭到卡顿。为避免卡顿，考虑下载后观看，因此找到了BBDown项目。但在看到感兴趣的视频后再手动下载，仍需等待一段时间。此脚本将自动下载关注列表中的UP主视频到本地，等到闲暇时直接打开本地文件夹即可挑选视频观看。

### 这个脚本的具体功能描述

* 将关注的up的UID手动写入一个本地txt文档后，每次运行本脚本，都会自动下载该txt文档中列出的up主上传的新视频到指定目录。
* （可选）因为BBDown会自动将有分p的视频下载到子文件夹中，本脚本可以将子文件夹中的视频自动挪出。
* （可选）因为本人拒绝一切竖屏视频，本脚本会在下载后自动删除一切竖屏视频。

### 如何使用这个脚本

* 下载并安装Python。
* 下载ffprobe (ffmpeg项目的一部分），并将其放置在脚本开头FFprobePath所指定的位置。（默认为.\ffmpeg\ffprobe.exe）
* 下载BBDown项目的可执行文件，将其放置在脚本开头BBDownPath所指定的位置（默认为.\BiliBiliCacher\bin\bbdown.exe），并根据该项目的文档配置BBDown。以下是个人关于如何配置BBDown的一些说明（针对1.60版本）：
<details>
 <summary>个人关于如何配置BBDown的一些说明（针对1.60版本）</summary>
  
  * 下载ffmpeg，并将其放置到BBDown文件夹内。
  * 在命令行中打开BBDown，使用login指令登录。（按Win+R，输入cmd后回车 - 在弹出窗口中输入cd 【BBDown.exe所处的路径名称】，如cd D:\BBDown-BilibiliAutoFollowDownloader\BBDown\，回车- 输入 BBDown login，回车- 扫描二维码登录 - 关闭窗口）。
  * 使用文本编辑器在BBDown/bin文件夹内新建文件BBDown.config，参照BBDown项目中的说明进行进一步配置。
  * 使用文本编辑器

</details>

* 更改脚本开头的CachePath和DownloadPath变量，使其符合你的使用习惯（默认为E:\BiliBiliCache\Cache和E:\BiliBiliCache）。DownloadPath为最终视频存储的位置。建议将CachePath和DownloadPath放在一个盘符中以避免无谓复制。
* 在在脚本开头FollowListPath指定的位置（默认为.\BiliBiliCacher\Followlist.txt）创建一个txt文档，在其中填入你想要追更的UP主的UID，每行一个。
* 如某UP主页网址为https://space.bilibili.com/869610/ ，则填入869610并点击回车，随后在第二行键入你想追更的第二个UP主的UID。
* 点击BilibiliFollowAutoDownloader.py执行首次运行以初始化。初始化将不会下载任何视频；只有首次运行后新上传的视频会被下载。
* 使用Task Scheduler/任务计划程序将此脚本设为定时运行（如每天一次），注意将起始目录设为脚本目录。
 <details>
 <summary>详细说明</summary>
  * 按Win+R，输入taskschd.msc后回车，打开Task Scheduler/任务计划程序。
  * 点击右侧“Create Basic Task/创建基本任务”。
  * 在弹出窗口中输入任务名称，点击下一步。
  * 设置Trigger/触发器，建议选择每日或当前用户登陆时，点击下一步。
  * 在Action/操作一栏选择“Start a program/启动程序”。
  * 在程序和脚本一栏点击浏览，找到BilibiliFollowAutoDownloader.py并点击打开。
  * 在“Start in/起始于”一栏输入脚本所在的目录，如D:\BBDown-BilibiliAutoFollowDownloader\。
  * 点击完成。

</details>

  * 当你有想要关注的新UP主时，将其UID填入FollowList.txt中，随后手动运行一次脚本进行初始化。

### 更新记录

#### 2022.08.02 第一个稳定版本

#### 2022.08.09 v0.2

重构了整个程序，通过改变索引方式提升了稳定性、效率、和和扩展性。**请完全删除第一个版本中的文件后重新下载。**

* 可以自由地添加/删除UP主
* 将FollowList.txt中的记载格式由主页链接（如https://space.bilibili.com/869610/ ）改为UID （如869610）。
* 在获取视频列表时会输出UP主昵称而非UID，方便用户理解。
* 如遇任何问题，请整体删除BBDown\VideoRecords文件夹。

#### 2024.3.14 v0.3

本来试图通过读取配置文件支持不同人的不同需求，想了想我自己爽就行了。于是有些可配置项写在了脚本开头，你也可以自行打开脚本更改。另一些新功能干脆没有设可配置项，但是你可以自己把它注释掉。

更改：
* 更改了一些依赖的默认保存位置
* 将许多变量（如下载目录）写死在了脚本开头，（放弃了用单独的配置文件存储变量）
* 梳理了命令行的输出，使之更易懂

新功能：
* BBDown会自动将分p下载为文件夹，现在会自动把文件夹展平（可在PostDownloadFix函数中关闭此功能）。
* 会在下载后自动删除竖屏视频（因为我自己不看）（可在PostDownloadFix函数中关闭此功能，或通过简单调整使其不下载横屏视频）（其实BBDown似乎有只解析不下载的功能，这个功能其实可以在下载前就决定不下载竖屏的）
* 为支持以上功能，视频会先下载到CachePath,然后再移动到DownloadPath。为减轻硬盘压力建议将两个路径设置在一个盘符下。

#### 2024.3.15 v0.3.1
新功能：
在FollowList.txt中自动添加UP主昵称备注以方便删除

### 已知的BUG

* 如某UP在被索引后删除了所有旧视频，随后上传了新视频，会触发数组越界闪退。
* 如某UP主在被索引时/检查更新时没有任何视频，会触发数组越界闪退。

### 计划中的新功能

- [*] 在FollowList.txt中自动添加UP主昵称备注以方便删除

-<del> [ ] 支持UP分类功能，下载至不同文件夹</del>
此功能被放弃。但是，因为目前FollowList.txt的路径和下载路径两个变量不再写死在脚本文件各处，而是在脚本开头由FollowListPath和DownloadPath两个变量声明，因此一个简单的workaround为将此脚本复制多份，为每一份分别指定不同的FollowListPath和DownloadPath即可。

- [ ] 自动标准化音频响度

  

