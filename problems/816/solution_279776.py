def maiores(lista, n):
    ''' funcao que dado os elementos de uma lista de numeros inteiros,
    retona outra lista com numeros da lista maiores que n 
    list, int ->list '''
    numeros = lista[:]
    if (n not in numeros):
        numeros.append(n)
        numeros.sort(reverse = True)
    l = numeros.index(n)
    return sorted(numeros[:l])