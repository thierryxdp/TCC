# transforma valores a e b na concatenação abba
#a=>str, b=>str
# str, str -> str
def concatenacao(a,b):
    """Une os valores de a e b na forma de abba"""
a=str
b=str
c=str.join(a,b,b,a)
if c in str:
    return c