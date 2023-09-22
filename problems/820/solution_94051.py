def posLetra(frase,letra,x):
    posicao=0
    ocorrencias=0
    while posicao<len(frase):
        if frase[posicao]!=letra and ocorrencias !=x:
            ocorrencias=ocorrencias+1
            posicao=posicao+1
        elif frase[posicao]==letra and ocorrencia==x:
            return ocorrencias
        else:
            return -1