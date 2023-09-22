def uppCons(frase):
    '''Recebe como entrada uma frase e retorna a 
    a frase com suas consoantes em maiúsculas.
    string -> string'''
    x = 0
    s = ''
    while x < len(frase):
        if frase[x] in 'bcdfghjklmnpqrstvxwyz':
            s += frase[x].upper()
            return s
        else:
            s += frase[x]
            return s
        
        x += 1