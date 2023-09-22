import math
def carros(p , v=5):
"" Funcao que calcula quantos veiculos (v) de capacidade padrao 5 sao necessarios para transportar (p) pessoas. ""
carros = (math.ceil) p/v
return carros