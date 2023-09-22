# transforma valores a e b na concatenação abba
#a=>str, b=>str, c=>str
# str, str -> str
  def concatenacao(a,b):
         """Une os valores de a e b na forma de abba"""
  return str(a) + str(b) + str(b) + str(a)