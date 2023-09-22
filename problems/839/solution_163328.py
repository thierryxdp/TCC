def carros(pessoas,capacidade=5):
    """Determinar quantos bombons dará para comprar, dados o dinheiro e o preço do bombom para realização da compra;
    int, int -> int"""
    return math.ceil(pessoas/capacidade)