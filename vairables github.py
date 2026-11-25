Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variable rules
a=50
print(a)
50
_=100
print(_)
100
d=100
p=50
>>> print(d+p)
150
>>> print(d,p)
100 50
>>> name="divya"
>>> print(name)
divya
>>> last_name="Sri"
>>> print(last_name)
Sri
>>> village="cherukupalli"
>>> print(village)
cherukupalli
>>> d,s,r=10,20,40
>>> print(d,s,r)
10 20 40
>>> print(d+s+r)
70
>>> p=60,33,23,75
>>> print(p)
(60, 33, 23, 75)
>>> d=100;p=55
>>> print(d,p)
100 55
>>> print(d+p)
155
>>> divya=sri=gradute
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    divya=sri=gradute
NameError: name 'gradute' is not defined
>>> x=y=z=divya
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x=y=z=divya
NameError: name 'divya' is not defined
>>> x=y=z=100
>>> print(x,y,z)
100 100 100
