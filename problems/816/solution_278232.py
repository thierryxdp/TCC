def maiores(lista, n):
    '''Função que recebe uma lista de inteiros e um número inteiro n e retorna outra lista
    com todos os números da lista original maiores que n; list, int -> list'''
    
    if n in lista and list.count(lista, n) < 2:
        list.sort(lista)
        return lista[list.index(lista, n)+1:]
    elif n in lista and list.count(lista, n) >= 2:
        list.sort(lista)
        return lista[list.index(lista, n)+list.count(lista, n):]
    else:
        list.append(lista, n)
        list.sort(lista)
        return lista[list.index(lista, n)+1:]