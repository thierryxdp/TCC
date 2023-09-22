def repetidos(lista):
    repetidos=[]
    posicao=0
    while posicao<len(lista):
        if lista[posicao]==lista[posicao+1]:
            repetidos=repetidos+1
    return repetidos