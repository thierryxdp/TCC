def media_matriz(m):
    soma = 0
    qtd = 0
    for linha in m:
        soma += sum(linha)
        qtd += len(linha)
    return round.2(soma/qtd)