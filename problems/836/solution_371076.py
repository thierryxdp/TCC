def busca(setor,matriz):
    '''
    list ----> list
    '''  
    retorno = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            dados = [matriz[i][0],matriz[i][1],matriz[i][3]]
            retorno+=[dados]
    return retorno