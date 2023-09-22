def media_matriz (M): 
    soma = 0
    tamanho = 0
    for linha in M:
        soma += sum(linha)
        tamanho += len(linha)
    return soma/tamanho