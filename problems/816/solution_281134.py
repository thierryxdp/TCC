def maiores(lista,n):
    '''Função que, dada uma lista qualquer e um número inteiro n, retorna uma lista com todos os números da lista original maiores que n.
list,int --> list'''
    lista_com_n = lista + [n]
    list.sort(lista_com_n)
    return lista_com_n[list.index(lista_com_n,n)+1:]