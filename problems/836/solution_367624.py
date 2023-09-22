def busca(setor, matriz):
    p = []
    for i in matriz:
        if i[2] == setor:
            p.append(i[:2]+i[:3])
    if p != []:
        return p
    return []