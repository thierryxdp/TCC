def busca(setor, lista):
    l = lista
    registro = []
    registro_maior = []
    for i in range(0,len(l)):
        if setor in l[i]:
            registro += ([l[i]])
    return registro