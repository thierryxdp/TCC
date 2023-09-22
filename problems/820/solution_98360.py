def posLetra(frase: str, letra:str, ocorrencia:int)-> int:
    """comentário"""
    i = 0
    posicao = []
    while i < len(frase):
        if frase[i] == letra:
            posicao += [1,]
            posicao = sum(posicao)
            if posicao == ocorrencia:
                return frase[posicao]
        i+=1
    else:
        return -1