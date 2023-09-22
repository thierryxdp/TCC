def maiores(lista_numero, n):
    '''Faça uma função que dada uma lista, retorna outra lista que contenha todos os números da lista original maiores que n, em ordem crescente
    lista, int -> lista'''
    ordem = (lista_numeros)
    list.append(ordem, n)
    list.sort(ordem)
    numero = ordem.index(n)
    lista = ordem[numero:]
    list.remove(lista, n)
    return lista