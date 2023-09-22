def faltante(lista):
    '''
    recebe uma lista de inteiros de 1 a n e retorna qual
    inteiro deste intervalo está faltando
    list->int
    '''
    i=1
    while i<len(lista)+2:
        if i in lista:
            i=i+1
        else:
            return i