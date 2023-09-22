def eh_quadrada(matriz):
    '''função que recebe uma matriz não-vazia e retorna se a mesma é ou não uma matriz quadrada. list -> bool'''
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna:
            return True
        else:
            return:False