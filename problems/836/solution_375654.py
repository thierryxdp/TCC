def busca(setor, matriz):
    
    retorno = []
    for x in matriz:
        if x[2] == setor:
            retorno.append(x[0:2] + x[3:])
    return retorno