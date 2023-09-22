def maiores(lista, n):
    '''função que recebe uma lista de números e um número n e retorna
    outra lista contendo todos os números da lista original maiores que
    n ordenados em ordem crescente.
    entrada:lista,int
    saída:lista'''
    list.append(lista,n)
    list.sort(lista)
    indice=list.index(lista,n)
    if n>lista[-2]:
        return []
    if lista[indice]!=lista[indice+1]:
        return lista[indice+1:]
    if lista[indice]==lista[indice+1]:
        return lista[indice+2:]