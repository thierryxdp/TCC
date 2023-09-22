def busca(setor,matriz):
    retorno_busca = []
    for linha in range(len(matriz)):
        if matriz[linha][2] == setor:
            item = [matriz[linha][0],matriz[linha][1],matriz[linha][2]]
            retorno_busca.append(item)
    return retorno_busca