Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
#positive striding
a="data scince"
a[::1]
'data scince'
b="machine learning"
b[::4]
'miln'
b[::6]
'men'
b[:9]
'machine l'
>>> a[7:]
'ince'
>>> a[5:11]
'scince'
>>> b[7:]
' learning'
>>> b[5:11]
'ne lea'
>>> b[::2]
'mcielann'
>>> c="i am divya from cherukupalli"
>>> c[5:10]
'divya'
>>> c[16:27]
'cherukupall'
>>> c[16:]
'cherukupalli'
>>> c[0:1]
'i'
>>> c[2:4]
'am'
>>> c[11:15]
'from'
>>> #negative striding
>>> d="cloud computing"
>>> d[-15:-16]
''
>>> a[2:14:3]
'tsn'
>>> d[2:14:3]
'o mt'
>>> d[1:13:4]
'l p'
>>> d[3:11:2]
'u op'
>>> d[5:14:5]
' u'
>>> z="i am da at codegnan vijayawada"
>>> z[-1:-9:-2]
'aaaa'
>>> z[-2:-12:-4]
'dyv'
>>> z[-10:--19:-2]
'v'
>>> z[-10:-19:-2]
'vnneo'
