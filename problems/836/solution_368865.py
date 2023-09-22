def busca(procura,matriz):
    i, j = 0,0
    for sub in matriz:
        if nome in sub:
            j = sub.index(nome)
            break
        i+=1
    else:
        return None
    
    return i,j