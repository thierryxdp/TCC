def busca(setor,matrix):
    
    lfinal=[]
    for func in matrix:
        if func[2]==setor:
            lfinal.append(func)
    return lfinal