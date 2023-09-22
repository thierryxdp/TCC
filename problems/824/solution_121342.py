def uppCons(frase):
    '''Recebe como entrada uma frase e retorna a frase com todas as suas
consoantes em maiúsculas e os demais caracteres exatamente como estavam na
frase original.'''
    i = 0
    vogal = ('a', 'e', 'i', 'o', 'u')
    frase2 = ' '
    while i < len(frase):
        if frase[i] not in vogal:
            str(frase2.upper(lista[i]))
        i = i+1

    return frase2