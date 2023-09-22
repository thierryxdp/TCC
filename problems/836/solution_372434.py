def busca(setor, matriz):
    x = 0
    for i in matriz:
        if i[2] == setor:
            list.pop(i, 2)
        else: 
            list.pop(matriz, x)
        x = x + 1    
    return i[2]