def busca(setor, matriz):
    lista_de_resultados = []
    linha_atual = 0
    linhas_totais = len(matriz)-1
    coluna_atual = 0
    colunas_totais = len(matriz[0])-1
    while linha_atual <= linhas_totais:
        while coluna_atual <= colunas_totais:
            if matriz[linha_atual][coluna_atual] == setor:
                lista_de_resultados.append(matriz[linha_atual][:2])
            coluna_atual += 1
        linha_atual += 1
        coluna_atual = 0
    
    return lista_de_resultados