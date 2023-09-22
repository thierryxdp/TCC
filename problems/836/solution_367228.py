def busca():
    r = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor in matriz[i]:
                matriz[i].remove(setor)
                r.append(matriz[i])
                
    return r