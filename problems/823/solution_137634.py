def faltante(lista):
    '''função que dada uma lista retorna o numero inteiro x do intervalo da lista mas que não pertence a 
    lista; list->int'''
    list.sort(lista)
    i=0
    n=1
    while i<len(lista):
        if lista[n-1]<lista[i]<lista[i+1]