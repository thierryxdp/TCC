def insere(lista_num,n):
    '''Função que dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclua n na posição correta, ou seja, de tal maneira que a lista continue
ordenada; list,int->list.'''
    lista_num.append(n)
    lista_num.sort()
    return lista_num