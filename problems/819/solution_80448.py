def filtraMultiplos(lista,n):
    '''Dada uma lista numeros e um numero n, retorna os numeros da lista que são numeros de n
list,int-->list'''
    multiplos=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            multiplos=multiplos+[lista[i]]
        i=i+1
    return multiplos