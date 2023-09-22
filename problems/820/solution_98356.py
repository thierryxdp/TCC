def posLetra(frase: str, letra:str, ocorrencia:int)-> int:
    """comentário"""
    i = 0
    posicao = [0,]
    while i < len(frase):
        if frase[i] == letra:
            posicao.append(1)
            posicao = sum(posicao)
            if posicao == ocorrencia:
                return posicao
        i+=1
    else:
        return -1