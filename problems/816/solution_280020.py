def maiores(lista1, n):
    '''Função recebe uma lista e um numero
    e retorna essa lista somadas ao numero N com apenas os 
    numeros maiores que N da lista, junto à N
    list, int -> int '''
    list.append(lista1, n)
    list.sort(lista1)
    indice = list.index(lista1, n) + 1
    frase_nova = lista1[indice:]
    return frase_nova