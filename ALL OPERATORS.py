Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#OPERATORS
#Arthemetic operator
a=200
b=10
print
<built-in function print>
print(a+b)
210
print(a-b)
190
print(a*b)
2000
print(a//b)
20
print(a/b)
20.0
print(a**b)
102400000000000000000000
print(a%b)
0
#assignment operator
a=20
b=5
a+=2
a
22
a-=2
a
20
a*=4
a
80
a//=2
a
40
a/=1
a
40.0
a%=3
a
1.0
b+=2
b
7
b-=2
b
5
b*=3
b
15
b//=2
b
7
b/=4
b
1.75
b%=2
b
1.75
#Comparision operator
a=20
b=10
a<b
False
a>b
True
b<a
True
b>a
False
a<=b
False
b<=a
True
a>=b
True
b>=a
False
a!=b
True
b!=a
True
a==b
False
b==a
False
#Logical operator
a=20
b=60
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or a>=b
True
a!=b or a==b
True
not True
False
not False
True
#Identify operator
a=100
type(a) is int
True
type(a) is not int
False
type(a) is float
False
type(a) is not float
True
type(a) is not complex
True
type(a) is str
False
type(a) is not str
True
b=4+2j
type(b) is not int
True
type(b) is not str
True
type(b) is complex
True
type(b) is not float
True
d=10
type(d) is int
True
type(d) is not complex
True
z=True
type(z) is bool
True
type(z) is not bool
False
#Membership operator
d=100,200,300,400,500,60,10
100 in d
True
20 in d
False
300 in d
True
100 not in d
False
10 not in d
False
60 in d
True
60 not in d
False
#Bitwise operator
a=20
b=5
a&b
4
a|b
21
a~b
SyntaxError: invalid syntax
~a
-21
a=2
b=4
a^b
6
bin(a)
'0b10'
>>> bin(b)
'0b100'
>>> 
>>> a^b
6
>>> #Left shift operator
>>> a=3
>>> bin(a)
'0b11'
>>> a<<2
12
>>> a=10
>>> b=10
>>> bin(b)
'0b1010'
>>> a<<2
40
>>> d=2
>>> bin(d)
'0b10'
>>> a<<2
40
>>> z=2
>>> bin(z)
'0b10'
>>> a<<3
80
>>> #Right shift operator
>>> a=4
>>> bin(a)
'0b100'
>>> f=2
>>> bin(f)
'0b10'
>>> a>>2
1
>>> h=3
>>> bin(h)
'0b11'
>>> h>>2
0
>>> g=4
>>> bin(g)
'0b100'
>>> g>>2
1
