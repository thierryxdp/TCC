def uppCons(frase):
    '''Recebe como entrada uma frase e retorna a 
    a frase com suas consoantes em maiúsculas.
    string -> string'''
    x = 0
    s = ''
    while x < len(frase):
        if frase[x] in 'bcdfghjklmnpqrstvxwyz':
            return ''.join(frase[x].upper())
        else:
            return s += frase[x]
        x += 1