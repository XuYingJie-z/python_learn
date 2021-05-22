# Iterator

迭代器的一些用法

## enumerate函数

enumerate函数可以在for循环时加上编号,非常有用
```python

>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))       # 下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

>>>seq = ['one', 'two', 'three']
>>> for i, element in enumerate(seq):
...     print(i, element)
... 
0 one
1 two
2 three
```
## 含有迭代器的类

通过`__iter__`实现迭代器，注意这里`deep_first()`函数里`self`是指`'Node({!r})'`，也就是`__repr__`方法返回的内容.	<br>
而`for c in self:`里`self`是指`__iter__(self)`方法返回的内容.

> 例子来源于python cookbook 4.4
```python
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
```
