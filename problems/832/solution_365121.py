def eh_quadrada(matriz):
    """Função que identifica se uma matriz é quadrada;
list->bool"""
    linha=len(matriz)
    quadrada=True
    for elemento in range(len(matriz)):
        if len(matriz[elemento])==linha:
            quadrada= True
        else:
            quadrada= False
    return quadrada