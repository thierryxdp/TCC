def maiores(lista_inteiros,n):
    '''Função que dada uma lista de números inteiros e um inteiro n, retorna uma lista dos números da lista original maiores que n
    list[int,...],int -> list[int,...]'''
    list.append(lista_inteiros,n)
    list.sort(lista_inteiros)
    return lista_inteiros[list.index(lista_inteiros,n)+1:]