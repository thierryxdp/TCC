def busca(setor, m):
    l1 = []
    for linha in m:
        for aij in linha:
            if aij in setor:
                list.remove(linha, aij)
                list.append(l1, setor)
  	return l1