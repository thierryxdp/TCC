def busca(setor,matriz):
    '''
    list ----> list
    '''  
    retorno = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            dados = [matriz[0],matriz[1],matriz[3]]
            retorno+=[dados]
    return retorno