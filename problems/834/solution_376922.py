def media_matriz(matriz):
    '''função que dada uma matriz, retorna a média dos números contidos na matriz. list -> float'''
    acum_coluna = 0
    soma = 0
    for i in matriz:
        acum_linha = 0
        for j in matriz[acum_coluna]:
            soma += matriz[acum_coluna][acum_linha]
            acum_linha += 1
        acum_coluna += 1
    return round(soma / (acum_linha * acum_coluna),2)