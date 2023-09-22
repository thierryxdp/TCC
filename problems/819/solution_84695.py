def filtraMultiplos(lista,n):
    '''funçao que recebe uma lista de numeros e um numero
    e retorna uma nova lista com os elementos da original que
    são divisiveis por este numero; list->list'''
    resultado=[]
    i=0
    while i<len(resultado):
        if lista(i)%n==0:
            lista=lista+(lista[i])
        i=i+1
    return resultado