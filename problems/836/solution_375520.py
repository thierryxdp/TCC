def busca(setor,matriz):
    for contatos in range(len(matriz)):
        for setor in contatos:
            if setor in matriz[contatos][2]:
                return matriz[contatos]
    return []