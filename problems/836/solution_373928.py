def busca(setor, matriz):
    matriz_nova = []
    for linha in matriz:
        if linha[2] == setor:
            del(linha[2])
            matriz_nova.append(linha)
    return matriz_nova