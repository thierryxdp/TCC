def maiores(lista,n):
    """Função que dada uma lista de números inteiros
       e um número inteiro n, retorna uma lista com
       os números da lista original maiores que n.
       list->list"""
    if n not in lista:
        list.sort(lista)
        list.append(lista,n)
        return lista[n-1:]