Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Datatyoe conversions
int(100)
100
int(100.99)
100
int("Kanagala")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("Kanagala")
ValueError: invalid literal for int() with base 10: 'Kanagala'
int(99+33j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(99+33j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
str(99)
'99'
str(7.59)
'7.59'
str("hello world")
'hello world'
str(33+23j)
'(33+23j)'
str(True)
'True'
str(False)
'False'
>>> float(200)
200.0
>>> float(4.000)
4.0
>>> float("i am visit tirupati")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    float("i am visit tirupati")
ValueError: could not convert string to float: 'i am visit tirupati'
>>> float(2+55j)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    float(2+55j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> complex(10)
(10+0j)
>>> complex(2.44)
(2.44+0j)
>>> complex("I eat brack fast")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    complex("I eat brack fast")
ValueError: complex() arg is a malformed string
>>> complex(4+21j)
(4+21j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> bool(99)
True
>>> bool(66.000000)
True
>>> bool("I am divya from cherukupalli")
True
>>> bool(5+1j)
True
>>> bool(True)
True
>>> bool(False)
False
