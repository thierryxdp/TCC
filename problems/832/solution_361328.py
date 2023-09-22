def eh_quadrada(matriz):
    """dada uma matriz, a função retorna um valor booleano indicndo se essa matriz é
    quadrada, ou não;
    list(list)->bool"""
    linha=len(matriz)
    coluna=len(matriz[0])
    if matriz==[]:
        return False
    elif linha==coluna:
        return True
    else:
        return False