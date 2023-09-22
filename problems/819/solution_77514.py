def filtraMultiplos(lista, n):
    '''Entre com uma lista de numeros e um numero inteiro para ser retornado
    uma lista com os numeros da lista que são divisivel pelo o numero de
    entrada
    Lista, Int -> Lista'''
    i=0
    lista2=()

    while i<len(lista):
        if lista[i]%n==0:
            lista2=lista2+(lista[i],)
        i=i+1

    return list(lista2)