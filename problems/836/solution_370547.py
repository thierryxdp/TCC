def busca(setor,matriz):
    
    lfinal=[]
    for func in matriz:
        if func[2]==setor:
            lfinal.append(func)
    return lfinal