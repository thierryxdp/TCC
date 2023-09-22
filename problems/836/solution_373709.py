def busca(setor,matriz):
    a = []
    m = matriz.copy()
    for i in m:
        if(i[2] == setor):
            del(i[2])
            a.append(i)
    return a