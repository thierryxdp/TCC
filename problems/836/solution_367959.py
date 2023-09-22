def busca(setor,matriz):
    i = 0
    j = 0
    M = []
    while i < len(matriz):
        for j in matriz[i]:
            if j == setor:
                matriz[i].remove(2)
            	M.append(matriz[i])
               	
        i = i + 1
    return M