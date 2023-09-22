def conta_numero(numero,matriz):
    '''essa função recebe um numero e uma matriz, e retorna quantas vezes esse numero foi repetido na matriz'''
    '''int, list -> int'''
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
    contador = 0

    for i in range(qtd_linhas):
        for l in range(qtd_colunas):
            if matriz[i][l] == numero:
                contador +=1
    return contador