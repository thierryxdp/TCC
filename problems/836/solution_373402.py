def busca(setor,P):
    colaboradores = []
    for linha in P:
        for aij in linha:
            if aij == setor:
                list.append(colaboradores,linha)
    return colaboradores