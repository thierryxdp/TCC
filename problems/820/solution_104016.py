def posLetra(Str, letra, numero):
    ''' Função que retorna a posição da string em que há ocorrência da letra
    str, str, int=>int'''
    i=0
    ocorrencia=0
    while i< len(Str):
        if Str[i] == letra:
            ocorrencia += 1
            if ocorrencia == numero:
                return Str.index(Str[i],i)
        contador += 1
        indice += 1
    return -1