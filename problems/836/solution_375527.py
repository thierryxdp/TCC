def busca(setor,matriz):
    for contatos in range(len(matriz)):
        if setor in matriz[contatos][1]:
            return matriz[contatos]
    return []