def carros(pessoas,capacidade=5):
    """Retorne quantos bombons dá pra comprar, dados o dinheiro e o preço do bombom para realização da compra;
    int, int -> int"""
    if (pessoas/capacidade)%2 == 0:
  		return pessoas//capacidade
    else:
        return (pessoas//capacidade) + 1