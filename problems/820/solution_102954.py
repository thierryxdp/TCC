def posLetra(palavra, letra, ocorrencias):
    '''Retorna a posição de uma dada letra, dentro de uma palavras e sua ocorrencia
    str, str, int -> int'''
    if str.count(palavra, letra) < ocorrencias:
        return -1

    i = 0
    encontradas = 0
    posLetra = -1
    
    while i < len(palavra) and encontradas < ocorrencias:
        if palavra[i] == letra:
            posLetra = (i-1)
            encontradas+= 1
        i+=1
        
    return posLetra