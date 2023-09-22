def carros (n_pessoas, capacidade=5):
"""Calcular a quantidade de carro necessária para  um grupo de n pesssoas
int -> int """
return math.ceil (n_pessoas/capacidade)