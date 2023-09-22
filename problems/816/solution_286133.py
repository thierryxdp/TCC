def maiores(lista_numero, n):
    '''Faça uma função que dada uma lista, retorna outra lista que contenha todos os números da lista original maiores que n, em ordem crescente
    lista, int -> lista'''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    numero = list.index(n)
    lista = lista_numero[numero:]
    list.remove(lista, n)
    return lista