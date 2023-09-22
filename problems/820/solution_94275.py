def posLetra(string, letra, num):
    """retorna a posicao da string em que a ocorrencia da letra esta """
    posicao = -1
    ocorr = 0
    for l in string:
        posicao += 1
        if l == letra:
            ocorr += 1
            if ocorr == num:
                    break
    if ocorr < num:
        posicao = -1
    return posicao