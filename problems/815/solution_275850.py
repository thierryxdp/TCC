def insere(lista_numero,n):
    '''lista que dada uma lista ordenada de numeros
    inteiros e um numero inteiro n, inclui n na posição
    correta'''
    l = list.append(lista_numero, n)
    l = list.sort(l)
    return l