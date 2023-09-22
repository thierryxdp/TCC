def busca(setor,matrix):
    lfinal=[]
    for func in matrix:
        if func[2]==setor:
            funcInf=func[:2]+[func[3]]
            lfinal.append(funcInf)
    return lfinal