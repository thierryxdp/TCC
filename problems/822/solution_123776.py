def repetidos(lista):
    repeticao=0
    posicao=0
    while posicao<len(lista):
        posicao+=1
        if lista[posicao]==lista[posicao+1]:
            repeticao=repeticao+1
    return repeticao