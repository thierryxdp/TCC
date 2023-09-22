def repetidos(lista):
    '''list->int'''
    posicao=0
    repeticao=0
    while posicao<len(lista):
        if lista[posicao-1]==lista[posicao]:
            repeticao=repeticao+1
    return repeticao