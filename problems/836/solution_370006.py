def busca(setor, matriz):
    lista_de_resultados = []
    linha_atual = 0
    linhas_totais = len(matriz)-1
    coluna_atual = 0
    colunas_totais = len(matriz[0])-1
    while linha_atual <= linhas_totais:
        while coluna_atual <= colunas_totais:
            if matriz[linha_atual][coluna_atual] == setor:
                contato_alvo = matriz[linha_atual]
                contato_alvo.pop(2)
                lista_de_resultados.append(contato_alvo)
            coluna_atual += 1
        linha_atual += 1
        coluna_atual = 0
    
    return lista_de_resultados