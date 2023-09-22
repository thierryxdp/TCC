# transforma valores a e b na concatenação abba
#a=>str, b=>str, c=>str
# str, str -> str
def concatenaçao (a, b):
 def retorno (c):
         """Une os valores de a e b na forma de abba"""
 a=input(str)
 b=input(str)
 c=str(a) + str(b) + str(b) + str(a)
 return c