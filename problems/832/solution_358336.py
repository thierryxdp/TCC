def eh_quadrada(matriz):
    """Função que, dada uma matriz (lista de lista)
    identifica se esta é ou não quadrada
    list -> bool"""
    eh = False
    if matriz == [] or len(matriz) == len(matriz[0]):
        eh = True
    return eh