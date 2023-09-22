def filtraMultiplos(numeros,n):
    '''Retorna uma lista com os
       elementos da lista original
       que são divisíveis por n;
       list,int->list'''
    lista=[]
    indice=0
    while indice<len(numeros):
        if numeros[indice]//n==1:
            list.append(lista,numeros[indice])
            indice=indice+1
        if numeros[indice]//n==2:
            list.append(lista,numeros[indice])
        if numeros[indice]//n==4:
            list.append(lista,numeros[indice])
    return list