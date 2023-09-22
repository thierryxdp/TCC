def busca(setor,matriz):
    func=[]
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            if setor in matriz[i][c]:
                func.append(matriz[i])
    if setor in func:
        for t in func:
            for b in func:
                if func[t][b]==setor:
                    func[t].remove(b)
    return func