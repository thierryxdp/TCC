def faltante(L):
    '''
    '''
    
    lista=[]
    proximo=0
    while proximo<(len(L)):
        if L[proximo]==L[proximo+1]:
            lista= lista+[]
        else:
            lista=lista+[L[proximo]]
        proximo=proximo+1
    return lista