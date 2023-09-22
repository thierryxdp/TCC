def busca(setor, lista):
    l = lista
    registro = []
    for i in range(0,len(l)):
        if setor in l[i]:
            del l[i][2]
            registro += [l[i]]
    return registro