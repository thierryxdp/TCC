def faltante(L):
    '''
    '''
    
    lista=[]
    proximo=0
    while proximo<len(L):
        if x[proximo]==x[proximo+1]:
            lista= lista+[]
        else:
            lista=lista+[x[proximo]]
        proximo=proximo+1
    return lista[0]