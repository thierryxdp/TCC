def insere(lista_numero,n):
    '''Função que recebe uma lista crescente composta por números inteiros e um número inteiro n
    e deve retornar uma nova lista porém incluindo n de maneira que a lista mantenha-se ordenada.
    list,int->list'''
    lista=lista_numero.append(n)
    x=list.sort(lista)
    return x