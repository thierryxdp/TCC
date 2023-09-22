def posLetra(frase,letra,x):
    posicao=0
    ocorrencias=0
    while posicao<len(frase):
        if frase[posicao]!=letra:
            posicao=posicao+1
        elif frase[posicao]==letra:
            ocorrencias=ocorrencias+1
            posicao=posicao+1
        elif ocorrencias==x:
            return ocorrencias
        else:
            return -1