def posLetra(frase,letra,ocorrencia):
    '''funcao que retorne qual posicao da string aquela ocorrencia da letra esta'''
    i = 0
    n = 0
    while i<len(letra) and n < ocorrencia:
        if frase[i] == letra:
            n = n +1
        i = i + 1
    if n < ocorrencia:
        return str(n)+str(letra)
    if n < ocorrencia:
        return str(n)+str(letra)
    else:
        return i-1