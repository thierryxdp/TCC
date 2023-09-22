def eh_quadrada(matriz):
    '''função que dada uma matriz da True se esta for uma matriz quadrada
       ou False, caso não for. matriz -> bool'''
    if (matriz == []):
        return True
    acumulador_coluna = 0
    for i in matriz:
        acumulador_linha = 0
        for j in matriz[acumulador_coluna]:
            acumulador_linha += 1
        acumulador_coluna += 1
    if (acumulador_linha == acumulador_coluna ** 2):
        return True, acumulador_linha, acumulador_coluna
    else:
        return False