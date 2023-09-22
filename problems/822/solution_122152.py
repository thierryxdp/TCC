def repetidos(lista):
    '''list->int'''
    posicao=1
    repeticao=0
    while posicao<len(lista):
        if lista[posicao]==lista[posicao-1]:
            repeticao=repeticao+1
    return repeticao