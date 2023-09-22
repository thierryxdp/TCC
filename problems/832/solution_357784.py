def eh_quadrada(matriz):
    '''list(list) - > list(list)'''
    qtdLinhas = len(matriz)
    qtdColunas = 0
    for m in matriz:
        qtdColunas = 0
        for n in m:
            qtdColunas += 1

    return qtdLinhas == qtdColunas