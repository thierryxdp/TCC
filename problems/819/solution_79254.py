def filtraMultiplos (lista,n):
    '''função que retorna numeros de uma lista que são
       multiplos de n
       list,int->list'''
    multiplos=[]
    n_lista=0
    while n_lista<len(lista):
        if lista[n_lista]%n==0:
            multiplos= multiplos+ [lista[n_lista]]
            n_lista= n_lista+1
        else:
            multiplos=multiplos
            n_lista= n_lista+1
    return multiplos