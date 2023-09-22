def maiores(lista,n):
    ''' Função que dada uma lista de números inteiros e um número inteiro , retorna outra lista que contenha todos os númros da lista riginal maiores que n
    lista, int->list'''
    if n not in lista:
        return sorted(lista)
    elif n in lista:
        lista=list(lista)>n
        lista=list[none]
    else: 
        return sorted(lista)