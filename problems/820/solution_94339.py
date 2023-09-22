def posLetra(frase,letra,n):
    ''' Retorna a posição da string aquela ocorrencia da letra está'''
    i = 0
    pos = 0
    while i < len(frase):
        if frase[i] == letra:
            pos = pos + 1
        i = i + 1
    return pos