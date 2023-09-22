def busca(setor,x):
    registro=[]
    i = 0
    while i < len(x):
        if setor in x[i]:
            registro.append(x[i])
        i = i + 1
    return registro