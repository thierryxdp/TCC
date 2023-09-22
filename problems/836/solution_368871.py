def busca(procura,matriz):
    i, j = 0,0
    mat = []
    for sub in matriz:
        if procura in sub:
            j = sub.index(procura)
            break
        i+=1
        mat.append(i)
        mat.append(j)
    else:
        return None
    
    return mat