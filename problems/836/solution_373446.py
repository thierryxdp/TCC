def busca(setor,P):
    colaboradores = []
    for linha in P:
        for aij in linha:
            if aij == setor:
                linha.pop(2)
                list.append(colaboradores,linha)
    return colaboradores