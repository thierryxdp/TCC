def busca(setor, matriz):
    x = 0
    y = matriz
    for i in y:
        if i[2] == setor:
            list.pop(i, 2)
        else: 
            list.pop(matriz, x)
        x = x + 1    
    return matriz