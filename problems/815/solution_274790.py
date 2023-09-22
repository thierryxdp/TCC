def insere(lista_numero,n):
    '''funcao que dada uma lista ordenada de numeros inteiros, e um numero inteiro n, inclua n na posição correta e a lista continue ordenada;
    list, int -> list'''
    lista1 = list.append(lista_numero,n)
    x = list.sort(lista1)
    return x