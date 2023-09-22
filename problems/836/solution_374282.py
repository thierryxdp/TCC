def busca(setor, lista):
    l = lista
    registro = []
    for i in range(0,len(l)):
        if setor in l[i]:
            registro += ([l[i]])
            list.del(registro,setor)
    return registro