def buscaSetor(setor, m):
    i = 0
    res = []
    while i < len(m):
        if m[i][2] == setor:
            res.append([m[i][0], m[i][1], m[i][3]])
        i += 1
    return res