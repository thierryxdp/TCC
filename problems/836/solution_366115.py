def busca(setor,matriz):
    func=[]
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            if setor in matriz[i][c]:
				T=matriz[i].index(setor)
                matriz[i].pop(T)
                func.append(matriz[i])
    return func