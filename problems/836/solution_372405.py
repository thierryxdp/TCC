def busca(nome,matriz):
    '''
    '''
    resposta=[]
    for linha in matriz:
        for el in linha:
            if nome in linha and el==nome:
                resposta+= matriz[list.index(matriz,linha)]
    return resposta