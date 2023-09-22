def maiores(lista,n):
    """Função que dada uma lista de números inteiros
       e um número inteiro n, retorna uma lista com
       os números da lista original maiores que n.
       list->list"""
    if n == [0]:
        list.append(lista,n)
        list.sort(lista)
        return lista[n:]