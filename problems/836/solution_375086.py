def busca(setor,x):
    registro=[]
    i = 0
    j = 0
    while i < len(x):
        if setor in x[i]:
            registro.append(x[i])
        i = i + 1
        while j < len(registro):
            registro[j].remove(setor)
            j = j + 1
    return registro