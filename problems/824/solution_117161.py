def uppCons(frase):
    '''Recebe como entrada uma frase e retorna
    a frase com todas as consoantes em maisculas.
    string -> string'''
    x = 0
    while x < len(frase):
        if frase[x] not in 'aeiou':
            ''.join(frase[x].upper())
        x += 1
        return frase