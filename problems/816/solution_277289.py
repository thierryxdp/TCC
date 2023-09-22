def maiores(lista, n):
    ''' funcao que dado os elementos de uma lista de numeros inteiros,
    retons numeros maiores de n 
    list, int ->list '''
    numeros = lista[:]
    if n  in numeros:
        numeros.append(n)
        numeros.sort()
        idx = numeros.index(n)
    return numeros[:idx:]