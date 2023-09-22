def conta_frases(texto):
    """Retorna a quantidade de frases em determinado texto. str-> list"""
a = len(str.split(texto,'.'))
b = len(str.split(texto,'!'))
c = len(str.split(texto,'?'))
d = len(str.split(texto,'...'))

if a < 2:
   a = 0
elif b < 2:
   b = 0
elif c < 2:
   c = 0
elif d < 2:
   d = 0
   return a+b+c+d