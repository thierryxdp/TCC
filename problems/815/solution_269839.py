def insere(lista_numero,n):
    '''função que dada uma lista ordenada de números inteiros e um número inteiro
    n retorna a lista com o numero n inserido e em ordem crescente
    list,int->list'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero