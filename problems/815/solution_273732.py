def insere(lista_numero,n):
    '''insere um número n inteiro dado de entrada em uma lista de numeros
    inteiros  dada de entrada e deixa os elementos em ordem crescente list->list'''
    lista_numero[2:2]=[n]
    return list.sort(lista_numero)