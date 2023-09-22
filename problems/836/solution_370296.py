def busca(setor, dados):
    res = []

    for pessoa in dados:
        if pessoa[2] == setor:
            res.append(pessoa)

    return res