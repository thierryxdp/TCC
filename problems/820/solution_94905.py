def posLetra(string, letra, num):
    '''Dado uma string, uma letra e um numero, retorna em que posicao da string a ocorrencia de numero num da letra esta.
    str, str, int -> int'''
    pos = []
    i = 0
    j = 0

    while i < len(string):
        if string[i] == letra:
            pos.append(i)
        i += 1

    while j <= len(pos):
        if j == num:
            return pos[num-1]
        j += 1
    return -1