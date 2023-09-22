def maiores(lista,n):
    """Função que dada uma lista de números inteiros
       e um número inteiro n, retorna uma lista com
       os números da lista original maiores que n.
       list->list"""
    lista = list.insert(lista,n,1)
    nova_lista =list.sort(lista)
    return nova_lista[n-1:]