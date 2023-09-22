def conta_numero(numero, matriz):
    '''verifica quantas vezes o numero dado aparece na matriz.
    int|float, matriz -> int'''
    vezes = 0
    linha_atual = 0
    linhas_totais = len(matriz)-1
    if linhas_totais < 0:
        return 0
    coluna_atual = 0
    colunas_totais = len(matriz[0])-1
    while linha_atual <= linhas_totais:
        while coluna_atual <= colunas_totais:
            if numero == matriz[linha_atual][coluna_atual]:
                vezes +=1
            coluna_atual += 1
        linha_atual += 1
        coluna_atual = 0
    return vezes