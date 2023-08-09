这是一个调用[BBDown](https://github.com/nilaoda/BBDown)自动下载关注列表中的UP主的新视频的Python脚本。仅适配Windows系统。

### 这个脚本试图解决什么问题

或许因为本人位于非中国大陆地区，在线播放B站4k视频时经常遭到卡顿。为避免卡顿，考虑下载后观看，因此找到了BBDown项目。但在看到感兴趣的视频后再手动下载，仍需等待一段时间。此脚本将自动下载关注列表中的UP主视频到本地，等到闲暇时直接打开本地文件夹即可挑选视频观看。详细的使用方法见页面最底部。

### 如何使用这个脚本

* 下载并安装Python。
* 下载BBDown项目的可执行文件，将其放置到BBDown文件夹内，并根据该项目的文档配置BBDown。以下是个人关于如何配置BBDown的一些说明（针对1.60版本）：
<details>
 <summary>个人关于如何配置BBDown的一些说明（针对1.60版本）</summary>
  
  * 下载ffmpeg，并将其放置到BBDown文件夹内。
  * 在命令行中打开BBDown，使用login指令登录。（按Win+R，输入cmd后回车 - 在弹出窗口中输入cd 【BBDown.exe所处的路径名称】，如cd D:\BBDown-BilibiliAutoFollowDownloader\BBDown\，回车- 输入 BBDown login，回车- 扫描二维码登录 - 关闭窗口）。
  * 使用文本编辑器在BBDown文件夹内新建文件BBDown.config，参照BBDown项目中的说明进行进一步配置。

</details>

* 在主目录的FollowList.txt中填入你想要追更的UP主的UID，每行一个。
  * 如某UP主页网址为https://space.bilibili.com/869610/ ，则填入869610并点击回车，随后在第二行键入你想追更的第二个UP主的UID。
* 点击BilibiliFollowAutoDownloader.py执行首次运行以初始化。初始化将不会下载任何视频；只有首次运行后新上传的视频会被下载。
* 使用Task Scheduler/任务计划程序将此脚本设为定时运行（如每天一次），**注意将起始目录设为脚本目录**。
 <details>
 <summary>详细说明</summary>
  * 按Win+R，输入taskschd.msc后回车，打开Task Scheduler/任务计划程序。
  * 点击右侧“Create Basic Task/创建基本任务”。
  * 在弹出窗口中输入任务名称，点击下一步。
  * 设置Trigger/触发器，建议选择每日或当前用户登陆时，点击下一步。
  * 在Action/操作一栏选择“Start a program/启动程序”。
  * 在程序和脚本一栏点击浏览，找到BilibiliFollowAutoDownloader.py并点击打开。
  * **在“Start in/起始于”**一栏输入脚本所在的目录，如D:\BBDown-BilibiliAutoFollowDownloader\BBDown\。
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

### 已知的BUG

* 如某UP在被索引后删除了所有旧视频，随后上传了新视频，会在67行处触发数组越界闪退。
* 如某UP主在被索引时/检查更新时没有任何视频，会在67行处触发数组越界闪退。

### 计划中的新功能

- [ ] 在FollowList.txt中自动添加UP主昵称备注以方便删除

- [ ] 支持UP分类功能，下载至不同文件夹

  

