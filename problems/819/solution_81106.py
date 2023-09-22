def filtraMultiplos(lista,n):
    '''funçao que dada uma lista vazia e um numero n,retorna uma lista contendo todos os numeros divisiveis por n da lista original; lista',int -> lista'''
    lista = []
    indice = 0
    while proximo < len(lista):
        if lista[indice]%n == 0 :
            lista = lista + (lista[indice])
        indice = indice + 1
    return multiplos