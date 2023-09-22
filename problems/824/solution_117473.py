def uppCons(frase):
    '''Recebe uma frase e retorna a frase com as consoantes
    em maisculas.
    string -> string'''
    i = 0
    tot = 0
    a = []
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            a.append(frase[i].upper())
        return a
    		
        i += 1