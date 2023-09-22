def busca(setor,matriz):
    retorno_busca = []
    for linha in range(len(matriz)):
        if matriz[linha][2] == setor:
            retorno_busca.append(matriz[linha])
    return retorno_busca