def busca(procura,matriz):
    i, j = 0,0
    for sub in matriz:
        if procura in sub:
            j = sub.index(procura)
            break
        i+=1
        matriz.remove('Contabilidade')
        matriz.remove('RH')
    else:
        return []
    
    return [matriz[i],matriz[j]]