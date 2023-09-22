def faltante(lista):
    '''função que retorna o numero inteiro que pertence ao intervalo de uma 1 a n'''
    '''list-->list'''
    list.reverse(lista)
    num=lista[0]
    list.sort(lista)
    i=0
    a=0
    while i<num:
        a=a+1
        if a!=lista[i]:
            return a
        i=i+1
    return i+1