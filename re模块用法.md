# re模块使用方法

## 1.基础使用方法
re是Python的一个第三方库。
为了能更直观的看出re的效果，我们先新建一个HTML网页文件（可直接复制）：
index.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <footer>
        <div>
            <div class="email">
                Email:re@qq.com
            </div>
            <div class="tel">
                手机号:88888888
            </div>
        </div>
    </footer>
</body>
</html>
```

re主要有三个功能：提取、匹配、替换。<br>
**1、提取findall：** <br>
`re.findall(【正则表达式】, 【被提取的字符串】)` <br>
注意：返回的类型是列表<br>

我们应如何取出上文index.html中的Email或者手机号呢：

```python
import re

with open('index.html', 'r', encoding='utf-8') as f:
    # 读取index.html
    html = f.read()
    # 把html中的换行符，去掉，也就是替换成空字符串，因为.不能匹配到换行符（这里也可以使用re.M  re.findall(pattern_1, html，re.M)
    html = re.sub('\n', '', html)
    print(html)
    # 定义正则表达式，注意括号
    pattern_1 = '<div class="email">(.*?)</div>'
    # re.findall(【正则表达式】,【被提取的字符串】)，返回类型是列表
    ret_1 = re.findall(pattern_1, html)
    # 字符串.strip()，可以去除首位的空格和换行符
    print(ret_1[0].strip())
```

**2、匹配match：**

`re.match(【正则表达式】, 【被匹配的字符串】)` <br>
注意： <br>
如果匹配成功，返回<class 're.Match'>对象； <br>
如果匹配不成功，返回None。 <br>


我们应如何编写定义密码的正则表达式呢： <br>

```python
import re

# 英文字母开头，可包括应为字母，数字、下划线，总位数6-16位
password_pattern = r'^[a-zA-Z][a-zA-Z0-9_]{5,15}$'
# 定义三个密码
pass1 = '1234567'
pass2 = 'k123456'
pass3 = 'k123'
# 打印测试结果，匹配成功返回re.Match对象，不成功返回None
print(re.match(password_pattern, pass1))
print(re.match(password_pattern, pass2))
print(re.match(password_pattern, pass3))
```

###  re.M 等的使用方法

| re.I | 使匹配对大小写不敏感                                           |
|------|----------------------------------------------------------------|
| re.L | 做本地化识别（locale-aware）匹配                               |
| re.M | 多行匹配，影响 ^ 和 $                                          |
| re.S | 使 . 匹配包括换行在内的所有字符                                |
| re.U | 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.        |
| re.X | 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。 |


## 2.具体使用方法

1、re.compile（pattern，flags = 0 ）

将正则表达式模式编译为正则表达式对象，可使用match()，search()以及下面所述的其他方法将其用于匹配

```python
>>> prog = re.compile('\d{2}') # 正则对象

>>> prog.search('12abc')
<_sre.SRE_Match object; span=(0, 2), match='12'>
>>> prog.search('12abc').group() # 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
'12'

>>> prog.match('123abc')
<_sre.SRE_Match object; span=(0, 2), match='12'>
>>> prog.match('123abc').group()
'12'
>>>
```


2、re.search（pattern，string，flags = 0 ）

　　扫描字符串以查找正则表达式模式产生匹配项的第一个位置 ，然后返回相应的match对象。None如果字符串中没有位置与模式匹配，则返回；否则返回false。请注意，这与在字符串中的某个点找到零长度匹配不同。

```python
#在这个字符串进行匹配，只会匹配一个对象
>>> re.search('\w+','abcde').group()
'abcde'
>>> re.search('a','abcde').group()
'a'
>>>
```

3、re.match（pattern，string，flags = 0 ）

如果字符串**开头**的零个或多个字符与正则表达式模式匹配，则返回相应的匹配对象。None如果字符串与模式不匹配，则返回；否则返回false。请注意，这与零长度匹配不同。

```python
# 同search,不过在字符串开始处进行匹配，只会匹配一个对象
>>> re.match('a','abcade').group()
'a'
>>> re.match('\w+','abc123de').group()
'abc123de'
>>> re.match('\D+','abc123de').group() #非数字
'abc'
>>>
```

4、re.fullmatch（pattern，string，flags = 0 ）

如果**整个字符串**与正则表达式模式匹配，则返回相应的match对象。None如果字符串与模式不匹配，则返回；否则返回false。请注意，这与零长度匹配不同。

```python
>>> re.fullmatch('\w+','abcade').group()
'abcade'
>>> re.fullmatch('abcade','abcade').group()
'abcade'
>>>

```

5、re.split（pattern，string，maxsplit = 0，flags = 0 ）

　　通过出现模式来拆分字符串。如果在pattern中使用了捕获括号，那么模式中所有组的文本也将作为结果列表的一部分返回。如果maxsplit不为零，则最多会发生maxsplit分割，并将字符串的其余部分作为列表的最后一个元素返回。

```python
>>> re.split('[ab]', 'abcd') # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
['', '', 'cd']
>>> re.split(r'\W+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split(r'(\W+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split(r'\W+', 'Words, words, words.', 1)
['Words', 'words, words.']
>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']



如果分隔符中有捕获组，并且该匹配组在字符串的开头匹配，则结果将从空字符串开始。字符串的末尾也是如此：

>>> re.split(r'(\W+)', '...words, words...')
['', '...', 'words', ', ', 'words', '...', '']
a = '135-688-251'
re.findall(r'(135)-([6-9]+)', a)
out:   [('135', '688')]  ## 匹配括号里的内容
re.findall(r'([1-9]+)', a)
out:   ['135', '688', '251']
```

6、re.findall（pattern，string，flags = 0 ）

　　以string列表形式返回string中pattern的所有非重叠匹配项。从左到右扫描该字符串，并以找到的顺序返回匹配项。如果该模式中存在一个或多个组，则返回一个组列表；否则，返回一个列表。如果模式包含多个组，则这将是一个元组列表。空匹配项包含在结果中。

```python
>>> re.findall('a', 'This is a beautiful place!')
['a', 'a', 'a']

```

7、re.finditer（pattern，string，flags = 0 ）

返回一个迭代器，该迭代器在string类型的RE 模式的所有非重叠匹配中产生匹配对象。 从左到右扫描该字符串，并以找到的顺序返回匹配项。空匹配项包含在结果中。

```python
>>> re.finditer('[ab]', 'This is a beautiful place!')
<callable_iterator object at 0x0000000000DCDA90> #迭代器对象
>>> ret=re.finditer('[ab]', 'This is a beautiful place!')
>>> next(ret).group() #查看下一个匹配值
'a'
>>> [i.group() for i in ret] #查看剩下所有匹配的值
['b', 'a', 'a']
```

8、re.sub（pattern，repl，string，count = 0，flags = 0 ）

　　返回通过用替换repl替换字符串中最左边的不重叠模式所获得的字符串。如果找不到该模式， 则返回的字符串不变。 repl可以是字符串或函数；如果是字符串，则处理其中的任何反斜杠转义。即，将其转换为单个换行符，将其转换为回车，依此类推。count参数表示将匹配到的内容进行替换的次数
复制代码
```python
>>> re.sub('\d', 'S', 'abc12jh45li78', 2) #将匹配到的数字替换成S,替换2个
'abcSSjh45li78'

>>> re.sub('\d', 'S', 'abc12jh45li78') #将匹配到所有的数字替换成S
'abcSSjhSSliSS'
```


9、re.subn（pattern，repl，string，count = 0，flags = 0 ）

执行与相同的操作sub()，但返回一个元组。(new_string, number_of_subs_made)

```python
>>> re.subn('\d', 'S', 'abc12jh45li78', 3)
('abcSSjhS5li78', 3)
```

10、re.escape(pattern)

escape中的所有字符图案，除了ASCII字母，数字和'_'。如果要匹配可能包含正则表达式元字符的任意文字字符串，这将很有用。

```python
>>> re.escape('python.exe\n')
'python\\.exe\\\n'
```

11、search（）与match（）方法

Python提供了两种基于正则表达式的原始操作： re.match()仅在字符串的开头匹配，re.search()检查匹配项，在字符串中的任何位置检查匹配项（这是Perl的默认设置）。

```python
>>> re.match("c", "abcdef") #Not match
>>> re.search("c", "abcdef") #match
<_sre.SRE_Match object; span=(2, 3), match='c'>
>>>

以开头的正则表达式'^'可用于search()限制字符串开头的匹配项：

>>> re.match("c", "abcdef") #Not match
>>> re.search("^c", "abcdef") #Not match
>>> re.search("^a", "abcdef") #match
<_sre.SRE_Match object; span=(0, 1), match='a'>
>>>
```
