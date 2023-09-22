def uppCons(frase):
    '''Função que recebe como entrada uma frase com suas consoantes
    em maiscula.
    string - string'''
    x = 0
    frase_up = ''
    while x < len(frase):
        if frase[x] in 'bcdfghjklmnpqrstvxwz':
            frase_up += str.upper(frase[x])
        else:
            frase_up += frase[x]
        x += 1
    return frase_up