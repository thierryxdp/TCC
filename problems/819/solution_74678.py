def filtraMultiplos(lista,n):
    '''recebe uma lista de numeros e um numero n, retorna uma nova lista com os numeros
    da lista originais que forem multiplos de n
    list,float-->list'''
    novalist=[]
    i=0
    while(i<len(lista)):
        if(lista[i]%n==0):
            list.append(novalist,lista[i])
        i+=1
    return novalist