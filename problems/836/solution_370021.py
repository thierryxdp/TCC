def busca(setor,matriz):
    lista_de_resultados = []
    linha_atual = 0
    linhas_totais = len(matriz)-1
    coluna_atual = 0
    colunas_totais = len(matriz[0])-1
    while linha_atual <= linhas_totais:
        while coluna_atual <= colunas_totais:
            contatoantes = matriz[linha_atual][:2]
            contatodepois = matriz[linha_atual][3:]
            contato = contatoantes + contatodepois
            lista_de_resultados.append(contato)
            coluna_atual += 1
        linha_atual += 1
        coluna_atual = 0
    return lista_de_resultados