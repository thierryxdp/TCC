def posLetra(frase, letra, numero):
    """Funcao que dada uma string uma letra e um numero retorna
    em que posição da frase a ocorrencia da letra esta
    str, str, int --> int"""
    posicao = 0
    ocorrencia = 1
    while posicao < len(frase):
        if letra == frase[posicao]:
            if ocorrencia == numero:
                x = posicao
            ocorrencia = ocorrencia + 1
        posicao = posicao + 1
    return x