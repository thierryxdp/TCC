from math import floor
def num_bombons(dinheiro, precoBombom):
    # Função que verifica o quanto de dinheiro tem e o preço do bombom, e retorna o numero de bombons que ele pode comprar
    # float, float -> int
    return floor(dinheiro/precoBombom)