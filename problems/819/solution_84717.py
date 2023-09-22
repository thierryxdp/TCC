def filtraMultiplos(lista,n):
    '''funçao que recebe uma lista de numeros e um numero
    e retorna uma nova lista com os elementos da original que
    são divisiveis por este numero; list,int->list'''
    lista1=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            lista1+= [lista[i],]
        i=i+1
    return lista1