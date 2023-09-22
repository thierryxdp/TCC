def uppCons(frase):
    '''Recebe como entrada uma frase e retorna a frase com todas as suas
consoantes em maiúsculas e os demais caracteres exatamente como estavam na
frase original.'''
    vogal = str('a', 'e', 'i', 'o', 'u')
    cons = not vogal

    return upper(cons)