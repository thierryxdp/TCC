def filtraMultiplos(lista,n):
    '''Dada uma lista de números, retorna uma nova lista com os números da primeira que são múltiplos de n'''
    '''list,int->list'''
    x=0
    multiplos=[]
    while x<len(lista):
        if lista[x]%n==0:
            list.append(multiplos,lista[x])
        x=x+1
    return multiplos