def busca(setor,x):
    registro=[]
    i = 0
    while i < len(x):
        if setor in x[i]:
            registro.append(x[i])
            del registro[2]
        i = i + 1
    return registro