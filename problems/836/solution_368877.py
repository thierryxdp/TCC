def busca(procura,matriz):
    i, j = 0,0
    for sub in matriz:
        if procura in sub:
            j = sub.index(procura)
            break
        i+=1
    else:
        return None
        del matriz[procura]
    return [matriz[i],matriz[j]]