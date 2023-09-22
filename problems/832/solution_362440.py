def eh_quadrada(matriz):
    '''
        recebe uma matriz na forma lista de listas e verifica se essa matriz e
        uma matriz quadrada retornando verdadeiro ou falso
        entrada: lista
        saida: booleano
    '''
    if (matriz == []):
        return 0 == 0
    else:
        linha = len(matriz)
        coluna = len(matriz[0])
        return (linha == coluna)