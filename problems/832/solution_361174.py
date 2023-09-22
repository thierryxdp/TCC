def eh_quadrada(matriz):
    """funcao que dada uma matriz, retorna se ela é uma matriz quadrada ou nao (uma matriz vazia é considerada quadrada)
    list(list)--->bool"""
    if (len(matriz)==2 and len(matriz[0])==2) or (len(matriz)==0 and len(matriz[0])==0):
        return True
    else:
        return False