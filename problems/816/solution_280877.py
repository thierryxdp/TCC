def maiores(lista,n):
    """Função que dada uma lista de números inteiros
       e um número inteiro n, retorna uma lista com
       os números da lista original maiores que n.
       list->list"""
    list.insert(lista,n,1)
    list.sort(lista)
    lista = str.split(lista)
    return lista[n:0]