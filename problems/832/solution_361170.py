def eh_quadrada(matriz):
    """funcao que dada uma matriz, retorna se ela é uma matriz quadrada ou nao
    list(list)--->bool"""
    if len(matriz)==2 and len(matriz[0])==2:
        return True