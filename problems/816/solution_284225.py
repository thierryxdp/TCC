def maiores(lista_inteiros, n):
    '''crie uma função que, dada uma lista de números inetiros e um número inteiro n, retorne unma nova lista que contenha os números da lista orginal maiores que n ordenados de forma crescente.list,int-->list.'''
    list.insert(lista_inteiros, 0, n)
    list.sort(lista_inteiros)
    lista = list.index(lista_inteiros, n)
    return lista_inteiros[lista + 1:]