def filtraMultiplos(lista,n):
    '''list,str-->list'''
    x=[]
    for i in range lista:
        lista[i]%n==0
        x+=1
    return x