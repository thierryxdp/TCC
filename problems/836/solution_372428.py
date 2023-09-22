def busca(setor, matriz):
    for i in matriz:
        if i[2] == setor:
            list.pop(i, 2)
        else: 
            list.pop(matriz, i)
    return matriz