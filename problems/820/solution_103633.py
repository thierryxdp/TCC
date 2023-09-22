def posLetra(frase, letra, numero):
    ''' função que retorna a posição da string em que a ocorrência da letra está
    str, str, int -> int
    '''
    palavras = list(frase)
    i = 0
    ocorrencia = 0
    while len(palavras) > i:
        if letra in palavras[i]:
            ocorrencia += 1
            if ocorrencia == numero:
                return i
        i += 1
    if ocorrencia < numero:
        return -1
    else:
        return ocorrencia