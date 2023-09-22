def posLetra(frase,letra,x):
    posicao=0
    ocorrencias=0
    while posicao<len(frase):
        if frase[posicao]==letra:
            ocorrencias=ocorrencias+1
        elif frase[posicao]==letra and ocorrencia==x:
            return ocorrencias
        posicao=posicao+1
        else:
            return -1