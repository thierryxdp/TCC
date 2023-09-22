def conta_numero(procura,matriz):
    """ a funcao busca os funcionarios de uma empresa por seus cargos nela"""
    i, j = 0,0
    for sub in matriz:
        if procura in sub:
            j = sub.index(procura)
            break
        i+=1
    else:
        return []
    
    return [matriz[i],matriz[j]]