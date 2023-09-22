def busca(setor, dados):
    res = []

    for pessoa in dados:
        if pessoa[2] == setor:
            res.append([pessoa[0], pessoa[1], pessoa[3]])

    return res