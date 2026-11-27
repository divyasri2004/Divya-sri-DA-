Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Negative indexing
>>> a="codegnan"
>>> a[-4]+a[-3]+a[-2]+a[-1]
'gnan'
>>> a[-8]+a[-7]+a[-6]+a[-5]
'code'
>>> a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'codegnan'
>>> b="work until you succeed"
>>> b[-11]+b[-10]+b[-9]
'you'
>>> b[-17]+b[-16]+b[-15]+b[-14]+b[-13]
'until'
>>> b[-22]+b[-21]+b[-20]+b[-19]
'work'
>>> b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b-1]
SyntaxError: unmatched ']'
>>> b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'succeed'
