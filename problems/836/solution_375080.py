def busca(setor,x):
    registro=[]
    while i < len(x):
        if setor in x[i]:
            registro.append(x[i])
            registro.remove(setor)
        i = i + 1
    return registro