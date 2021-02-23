# os 模块使用方法
1. os.name ——name顾名思义就是'名字'，这里的名字是指操作系统的名字，如Windows 返回 'nt'; Linux 返回'posix'。**注意该命令不带括号。**

2. os.getcwd() ——全称应该是'get current work directory'，获取当前工作的目录，如：返回结果为：'C:\\Program Files\\Python36'。注意该命令带括号，除了第一个命令不带括号之外，以下命令基本都带括号。

> os.chdir(path)——'change dir'改变目录到指定目录 

3. os.listdir(path)  ——列出path目录下所有的文件和目录名。Path参数可以省略

4. os.remove(path)——删除path指定的文件，该参数不能省略。

5. os.rmdir(path)——删除path指定的目录，该参数不能省略。

6. os.mkdir(path)——创建path指定的目录，该参数不能省略。

> **注意：这样只能建立一层，要想递归建立可用：os.makedirs()**

7. os.path.isfile(path)——判断指定对象是否为文件。是返回True,否则False

8. os.path.isdir(path)——判断指定对象是否为目录。是True,否则False

9. os.path.exists(path)——检验指定的对象是否存在。是True,否则False.

10. os.path.split(path)——返回路径的目录和文件名，即将目录和文件名分开，而不是一个整体。此处只是把前后两部分分开而已。就是找最后一个'/'。

11. os.system(cmd)——执行shell命令。返回值是脚本的退出状态码，0代表成功，1代表不成功

13. os.path.getsize()——获得文件的大小，如果为目录，返回0

14. os.path.abspath()——获得绝对路径。

15. os.path.join(path, name)—连接目录和文件名，与os.path.split(path)相对。

16.os.path.basename(path)——返回文件名

17. os.path.dirname(path)——返回文件路径 
