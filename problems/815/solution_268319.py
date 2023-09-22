def insere(lista_numero,n):
    """ dada uma lista ordenada(crescente) de numeros inteiros e um numero n, inclua n na posição correta"""
    a= list.extend(lista_numero,n)
    b= list.sort(a)
    return b