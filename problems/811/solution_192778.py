Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
help(dic)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    help(dic)
NameError: name 'dic' is not defined. Did you mean: 'dir'?
help(dictionary)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    help(dictionary)
NameError: name 'dictionary' is not defined
L=[1,2,3,4,5]
L[::2] = teste
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    L[::2] = teste
NameError: name 'teste' is not defined
inter = L
inter
[1, 2, 3, 4, 5]
L[::2] = inter
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    L[::2] = inter
ValueError: attempt to assign sequence of size 5 to extended slice of size 3
L
[1, 2, 3, 4, 5]
inter
[1, 2, 3, 4, 5]
I=[11,12]
inter = L+I
inter
[1, 2, 3, 4, 5, 11, 12]
L[::2]=inter
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    L[::2]=inter
ValueError: attempt to assign sequence of size 7 to extended slice of size 3
inter=L[::2]
inter
[1, 3, 5]
L
[1, 2, 3, 4, 5]
I
[11, 12]
inter = L + I
inter
[1, 2, 3, 4, 5, 11, 12]
inter[::2]=L
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    inter[::2]=L
ValueError: attempt to assign sequence of size 5 to extended slice of size 4

========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py =========
pontos_por_time([['Flamengo', 'Corinthians', [3,0]],['Corinthians', 'Flamengo', [2,0]]])
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    pontos_por_time([['Flamengo', 'Corinthians', [3,0]],['Corinthians', 'Flamengo', [2,0]]])
  File "C:/Users/nicho/Desktop/teste machineteaching.py", line 7, in pontos_por_time
    lista = [[dict.keys(time1, time2), [goltime1, goltime2]], [dict.keys(time2, time1), [goltime2, goltime1]]]
NameError: name 'time1' is not defined

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
pontos_por_time([['Flamengo', 'Corinthians', [3,0]],['Corinthians', 'Flamengo', [2,0]]])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    pontos_por_time([['Flamengo', 'Corinthians', [3,0]],['Corinthians', 'Flamengo', [2,0]]])
  File "C:/Users/nicho/Desktop/teste machineteaching.py", line 12, in pontos_por_time
    return dict.itens
AttributeError: type object 'dict' has no attribute 'itens'. Did you mean: 'items'?

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
pontos_por_time([['Flamengo', 'Corinthians', [3,0]],['Corinthians', 'Flamengo', [2,0]]])
'Flamengo'

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
pontos_por_time([['Flamengo', 'Corinthians', [3,1]], [4,2]])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    pontos_por_time([['Flamengo', 'Corinthians', [3,1]], [4,2]])
  File "C:/Users/nicho/Desktop/teste machineteaching.py", line 14, in pontos_por_time
    dicionario = {str(time1):time1j1+time1j2,str(time2):time2j1+time2j2}
TypeError: unsupported operand type(s) for +: 'int' and 'str'

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
pontos_por_time([['Flamengo', 'Corinthians', [3,1]], [4,2]])
{'Flamengo': 7, 'Corinthians': 3}

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
pontos_por_time([['Flamengo', 'Corinthians', [3,1]], [4,2]])
{'Flamengo': 6, 'Corinthians': 0}

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
pontos_por_time([['Flamengo', 'Corinthians', [3,0]],['Corinthians', 'Flamengo', [2,0]]])
{'Flamengo': 6, 'Corinthians': 0}

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
colchao([10,12,13], 10, 9)

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
colchao([10,12,13], 10, 9)
<class 'bool'>

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
colchao([10,12,13], 10, 9)
True

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
colchao([10,12,13], 10, 9)
True
colchao([10,12,13], 10, 10)
True

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
colchao([10,12,13], 10, 10)
True

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
colchao([10,12,13], 10, 10)
True

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
colchao([10,12,13], 10, 10)
True

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
colchao([10,12,13], 10, 10)
True
colchao([10,12,13], 10, 11)
True
colchao([10,12,13], 11, 11)
True
colchao([11,12,13], 10, 10)
True

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
colchao([11,12,13], 10, 10)
True

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
colchao([11,12,13], 10, 10)
False
colchao([11,12,13], 10, 11)
False
colchao([11,12,13], 10, 15)
False
colchao([11,12,13], 11, 15)
True

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========
colchao([11,12,13], 11, 15)
True

=========== RESTART: C:/Users/nicho/Desktop/teste machineteaching.py ===========