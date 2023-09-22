def filtraMultiplos(lista,n):
    '''função que filtra os números da lista 
    que sejam múltiplos de um número n
    valor de entrada: lista, int
    valor de saída: int'''
    multiplos=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            multiplos= multiplos+[lista[proximo],]
        proximo= proximo+1
    return multiplos