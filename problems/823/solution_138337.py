def faltante(L):
    '''
    ex: [1,2,4,5,6]
    '''
    
    
    
    lista=[]
    proximo=0
    while proximo<(len(L)-1):
        if L[proximo]!=L[proximo+1]-1:
            lista=lista+[proximo+2]
        if L[proximo]==L[proximo+1]-1:
            lista=lista+[L[-1]+1]
        proximo=proximo+1
    return lista[0]