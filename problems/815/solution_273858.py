def insere(lista_numero,n):
    '''função que dada uma lista ordenada de numeros inteiros inclui n
    na posição correspondente de forma que a lista continue ordenada; 
    list, int->list'''
    list.sort(lista_numero)
    a = (n-1)
    indice = list.index(lista_numero,a)
    return list.incert(lista_numero,indice,n)