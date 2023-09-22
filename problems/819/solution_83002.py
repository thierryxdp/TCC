def filtraMultiplos(lista,n):
    '''função que recebe como entrada uma lista de números e 
    um número n, retornando os múltiplos desse número n'''
    n=()
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%2 == 0:
            n = n + (lista[proximo],)
        proximo=proximo+1
    return multiplos