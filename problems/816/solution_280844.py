def maiores(lista,n):
    """Função que dada uma lista de números inteiros
       e um número inteiro n, retorna uma lista com
       os números da lista original maiores que n.
       list->list"""
    lista = []
    lista = list.append(lista,n)
    lista = list.sort(lista)
    return lista[n:]