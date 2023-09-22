def posLetra(frase: str, letra:str, ocorrencia:int)-> int:
    """comentário"""
    i = 0
    posicao = []
    while i < len(frase):
        if frase[i] == letra:
            posicao += [frase[i],]
            posicao = len(posicao)
        if posicao == ocorrencia:
                return frase.index(frase[i], i)
        i+=1
    else:
        return -1