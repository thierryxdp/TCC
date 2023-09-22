def eh_quadrada(matriz):
    """Função identifica se a matriz dada é quadrada ou não;
       list->bool
       Parametros:
       matriz: uma matriz qualquer
    """
    vazia=[]
    if matriz==vazia:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False