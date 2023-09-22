def maiores(lista , n):
    '''recebe uma lista de inteiros no 1 arg e retorna uma lista
    com os os caracteres dessa lista maiores do que n
    list , int -> list'''
    
    list.append(lista , n)
    list.sort(lista)

    novalista = lista[list.index(lista , n)+1:]

    return novalista