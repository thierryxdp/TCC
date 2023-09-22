def posLetra(frase: str, letra:str, ocorrencia:int)-> int:
    """comentário"""
    i = 0
    posicao = 0
    while i < len(frase):
        if frase[i] == letra:
            posicao += 1
            if posicao == ocorrencia:
                return string.index(string[indice], indice)
        i+=1
    else:
        return -1