def busca(matriz,setor):
    dados = []
    for linha in matriz:
        if setor in linha:
            list.remove(linha,setor)
            list.append(dados, linha)
    if len(dados) > 0:
        return dados