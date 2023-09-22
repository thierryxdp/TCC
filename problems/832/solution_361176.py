def eh_quadrada(matriz):
    """funcao que dada uma matriz, retorna se ela é uma matriz quadrada ou nao (uma matriz vazia é considerada quadrada)
    list(list)--->bool"""
    if len(matriz)==len(matriz[0]) or len(matriz)==0:
        return True
    else:
        return False