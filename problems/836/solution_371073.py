def busca(setor,matriz):
    '''
    list ----> list
    '''  
    retorno = []
    for i in range(len(matriz)):
        if matriz[i] == setor:
            dados = matriz-matriz[2]
            retorno+=[dados]
    return retorno