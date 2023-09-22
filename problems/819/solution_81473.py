def filtraMultiplos(lista,n):
    '''Função que recebe uma lista de numeros e um numero n. E retorna os multiplos de n dentro da lista
       list,int->list
    '''
    i=0
    listaMultiplos=[]
    while len(lista)<i:
        if (lista[i]%n)==0:
            listaMultiplos=listaMultiplos + lista[i]
            i=i+1
    return listaMultiplos