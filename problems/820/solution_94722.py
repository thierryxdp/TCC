def posLetra(string, letra, num):
    '''Faça uma função posLetra que recebe como entrada uma string, uma letra, e um número que indica a
ocorrência desejada da letra (1 para primeira ocorrência, 2 para segunda, etc). Sua função deve retornar
em que posição da string aquela ocorrência da letra está. Caso exista menos ocorrências da letra do que
a ocorrência pedida, a função deve retornar -1.'''
    #str > int
    pos = string.find(letra)
    while pos >= 0 and num > 1:
        pos = string.find(letra, pos + 1)
        num -= 1
    return pos