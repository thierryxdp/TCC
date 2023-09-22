def repetidos(lista):
    '''list->int'''
    posicao=0
    repeticao=0
    while posicao<len(lista):
        if lista[posicao]==lista[posicao-1]:
            repeticao=repeticao+1
        posicao=posicao+1
    return repeticao