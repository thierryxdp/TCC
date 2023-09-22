def posLetra(s, l, n):
    '''Recebe como entrada uma string, uma letra e um número que indica a
ocorrência desejada da letra. A função retorna em que posição da string aquela
ocorrência da letra está.'''
    pos = s.find(l)
    while pos >= 0 and n > 1:
        pos = s.find(l, pos + 1)
        n -= 1
    return pos