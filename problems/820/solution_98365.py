def posLetra(frase: str, letra:str, ocorrencia:int)-> int:
    """comentário"""
    i = 0
    posicao = []
    while i < len(frase):
        if frase[i] == letra:
            posicao += ['a',]
            posicao = sum(posicao)
            if posicao == ocorrencia:
                return frase.index(frase[i], i)
        i+=1
    else:
        return -1