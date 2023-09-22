def busca(setor, matriz):
    lista = []
    
    for i in range(len(matriz)):
        if setor in matriz[matriz.index(i)]:
            lista.append(matriz[matriz.index(i)])
    
    return lista