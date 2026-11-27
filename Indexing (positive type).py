Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[0}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[0]
'v'
a[1]
'i'
>>> a[2]
'j'
>>> a[3]
'a'
>>> a[4]
'y'
>>> a[5]
'a'
>>> a[6]
'w'
>>> a]7]
SyntaxError: unmatched ']'
>>> a[7]
'a'
>>> a[8]
'd'
>>> a[9]
'a'
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[9]
'vijayawaa'
>>> a="Time is precious"
>>> a[0]
'T'
>>> a[0]+a[1]+a[2]+a[3]
'Time'
>>> a[5]+a[6]
'is'
>>> a[8]+a[9]+a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'precious'
>>> a[4]+a[7]
'  '
>>> a="Vijayawada is royal city"
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]
'Vijayawad'
>>> a[10]+a[11]
' i'
>>> a[9]+a[10]+a[11]
'a i'
>>> a[11]+a[12]
'is'
>>> a[14]+a[15]+a[16]+a[17]+a[18]
'royal'
>>> a[20]+a[21]+a[22]+a[23]
'city'
>>> a[10]+a[13]+a[19]
'   '
