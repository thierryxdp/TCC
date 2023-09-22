def filtraMultiplos(lista,numero):
    '''list,int->list'''
    proximo=0
    divisores=[]
    while proximo<len(lista):
        if lista[proximo]%numero==0:
            divisores=divisores + [lista[proximo]]
            proximo=proximo+1
    return divisores