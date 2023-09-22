def uppCons(frase):
    '''Recebe uma frase e retorna com todas as suas consoantes em maiúsculas
    str -> str'''
    i = 0
    con = ' '
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnopqrstuvwxyzç':
            con = con + frase[i].upper()
        else:
            con = con + frase[i]
        i = i + 1
    return con