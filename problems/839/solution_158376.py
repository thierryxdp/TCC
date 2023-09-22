import math
def carros(pessoas,capacidade=5):

   '''numero de pessoas possiveis com capacidade maxima em carro de 5,
   (entr-int,saida-int)
'''

   return math.ceil(pessoas / capacidade)