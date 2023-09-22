def posLetra(frase, letra, numero):
    """Funcao que dada uma string uma letra e um numero retorna
    em que posição da frase a ocorrencia da letra esta
    str, str, int --> int"""
    posicao = 0
    ocorrencia = 0
    x = 0
    while posicao < len(frase):
        if letra == frase[posicao]:
            ocorrencia = ocorrencia + 1
            if ocorrencia == numero:
                x = posicao
        posicao = posicao + 1
    if ocorrencia < 1:
        x = -1
    return x