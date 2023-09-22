def filtraMultiplos(numeros, n):
    '''retorna os numeros da lista que sao multiplos do numero n
list[int], int-> list'''
    i=0
    multiplos=[]
    while i<len(numeros):
        if numeros[i]%n==0:
            list.append(multiplos,numeros[i])
        i=i+1
    return multiplos