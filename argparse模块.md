# 脚本参数传递argparse模块使用方法

argparse模块用来解析python脚本参数 <br>

使用方法：
* 1：import argparse

* 2：parser = argparse.ArgumentParser()

* 3：parser.add_argument()

* 4：parser.parse_args()

```python

import argparse   

description = "这是一个示例脚本"                   # 
parser = argparse.ArgumentParser(description=description)        # 这里会自动生成-h和--help参数，显示的内容久是description的内容
                                                                     
parser.add_argument('-v', '--verti', help = "这是一个示例参数")       # help是参数的描述
# 此外，还可以添加default（默认值）和type参数
# parser.add_argument('-v', '--verti', type=str, default='aaa' help = "这是一个示例参数")  


if __name__ == '__main__':
    args = parser.parse_args()
    print(args.verti)            #arg.v好像也可以


```

用argparse模块让python脚本接收参数时，加入action则该参数返回一个布尔值，即`action='store_true'`的时候`脚本.py -b`的args.base返回`True`，`脚本.py `，也就是不带-b的时候args.base返回一个`False`

```python
# action='store_true' or action='store_false' 引号要带着
parser.add_argument('-b', '--base', action='store_true', help = "这是一个示例参数")  
# 后面就可以用if语句进行分支
if args.base:
  pass
else:
  pass

```





