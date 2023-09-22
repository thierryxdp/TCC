import math
def carros(qntd_pes,capcdd):
   """Função que retorna a quantidade necessária de carros, com capacidade x, para uma determinada quantidade de pessoas."""
   return math.ceil(qntd_pessoas/capcdd)