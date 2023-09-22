def filtraMultiplos(lista,n):
    '''Recebe uma lista de números 'lista' e um número 'n' e retorna uma nova lista contendo os elementos de 'lista' que são divisíveis por 'n'; list->list'''
    numero=0
    retorno=[]
    while numero<len(lista):
        if lista[numero]%n==0:
            retorno=retorno+lista[numero]
        numero=numero+1
    return retorno