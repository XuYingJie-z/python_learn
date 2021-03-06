# 如何写class

### 1.利用super函数调用父类方法，然后在此基础上添加其他内容 <br>

例：重写一个list类

```python

class lis(list):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)   ## 注意这里super函数后面__init__和 上面def __init__传入参数的区别
    def insert(self, index, object):
        print(f"I\'m insert {object}")    # 这里相当于在原有函数基础上添加了内容
        super().insert(index, object)

a = lis([0,1,2])

>>>print(a)
[0,1,2]

>>>a.insert(1,2)
I'm insert 2 

>>>a
[0, 2, 1, 2]
## 这里用dir(a)或者dir(lis)可以看到lis继承了list的所有方法，也就是没有在lis类中改动的方法都原样继承了，比较方便
>>>dir(a)
>>>a[0]
0
```

### 类中的参数传递

直接看代码

```python
class example:
    def __init__(self,value):
        # value要在实例化类的时候传入,此处如果不将value传递给self.value的话，后续再定义的函数是无法调用value这个值的
        self.value = value
    def sum_d(self):
        return self.value **2   # 此处若是写成value ** 2的话会报错，显示value未定义

```
