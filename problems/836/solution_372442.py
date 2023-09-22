def busca(setor, matriz):
    y = []
    for i in matriz:
        for j in i:
            if j == setor:
                list.remove(i, j)
                list.append(y, i)      
    return y