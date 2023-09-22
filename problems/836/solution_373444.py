def busca(setor,P):
    colaboradores = []
    linha_mod = []
    for linha in P:
        for aij in linha:
            if aij == setor:
                list.append(linha_mod,linha[0])
                list.append(linha_mod,linha[1])
                list.append(linha_mod,linha[3])
    list.append(colaboradores,linha_mod)
    return colaboradores