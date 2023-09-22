def busca(setor,matriz):
    func=[]
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            if setor in matriz[i][c]:
               (func.append(matriz[i]))
                for t in range(len(func)):
                    for z in range(len(func[0])):
                        if func[t][z]==setor:
                            func.remove(z)
    return func