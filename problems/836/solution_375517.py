def busca(setor,matriz):
    for contatos in range(len(matriz)):
        if setor in agenda[contatos][2]:
            return agenda[contatos]
    return []