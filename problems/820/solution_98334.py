def posLetra(frase: str, letra:str, ocorrencia:int)-> int:
    """comentário"""
    i = 0
    posicao = 0
    while i < len(frase):
        if frase[i] == letra:
            posicao += 1
            if posicao == ocorrencia:
                return posicao[i]
            else:
                return -1