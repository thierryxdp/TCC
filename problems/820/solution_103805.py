def posLetra(frase, letra, ocorrencia):
    """Recebe uma frase, uma letra e um num de ocorrencia, 
    e retorna a posicao da string
    str, str, int --> int"""
    i = 0
    aparicao = 0
    while i < len(frase):
        if frase[i] == letra:
            aparicao += 1
            if aparicao == ocorrencia:
                return i
            else:
                i += 1
        else:
            i += 1
    return -1