def eh_quadrada(matriz):
    """A função recebe uma matriz, e tem de identificar se
    a mesma é quadrada ou não. Considerando que a matriz
    vazia (sem nenhuma linha, nem coluna) é considerada
    quadrada. A função booleana deve retornar True para
    matriz quadrada e False no caso contrário."""
    
    i=0
    linha=str(len(matriz))
    coluna=str(len(matriz[i]))
    
    if linha in coluna:
        return True
    else:
        return False