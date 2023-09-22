def eh_quadrada(matriz:list)-->bool:
    """dada uma matriz como entrada, a função retorna True se ela for quadrada
    e False caso contrário. Matrizes vazias são consideradas quadradas.
    list-->bool
    
    Parâmetros
    matriz: lista de listas contendo as linhas de uma matriz
    """
    if matriz==[]:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False