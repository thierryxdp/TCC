def media_matriz(matriz):
    lista_de_numeros = []
    linha_atual = 0
    linhas_totais = len(matriz)-1
    coluna_atual = 0
    colunas_totais = len(matriz[0])-1
    while linha_atual <= linhas_totais:
        while coluna_atual <= colunas_totais:
            lista_de_numeros.append(matriz[linha_atual][coluna_atual])
            coluna_atual += 1
        linha_atual += 1
        coluna_atual = 0
    media = round(sum(lista_de_numeros)/len(lista_de_numeros),2)
    return media