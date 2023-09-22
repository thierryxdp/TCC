import math
def carros(pessoas,capacidade=5):
    """Retorne quantos bombons dá pra comprar, dados o dinheiro e o preço do bombom para realização da compra;
    int, int -> int"""
  	return math.ceil(pessoas/capacidade)