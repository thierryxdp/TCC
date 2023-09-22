def busca(setor, matriz):
    L = []; M = matriz.copy()
    
    for x in M:
        if x[2] == setor:
            del x[2]
            L.append(x)
    return L