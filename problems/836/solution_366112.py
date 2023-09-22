def busca(setor,matriz):
    func=[]
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            if setor in matriz[i][c]:
				matriz[i].pop(setor)                
                func.append(matriz[i])
    return func