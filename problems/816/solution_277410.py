def maiores(lista,n):
    ''' Função que dada uma lista de números inteiros e um número inteiro , retorna outra lista que contenha todos os númros da lista riginal maiores que n
    lista, int->list'''
    if n not in lista:
        return list.sort(lista)
    else:
        lista=list.append(lista,n)
        list.sort(lista)
        posicao=list.index(lista,n)
        return list[posicao+1:]