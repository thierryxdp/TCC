def repetidos(lista):
    '''
    valor de entrada:
    valor de saída:  '''
    i=1
    resposta=0
    while i<len(lista):
        if lista[1]==lista[i-1]:
            resposta= resposta+1
        i=i+1
    return resposta