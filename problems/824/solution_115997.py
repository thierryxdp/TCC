def uppCons(frase):
    '''Função que retorna a frase com as consoantes em maiusculo
    str -> str'''
    c = ''
    i = 0
    while i <len(frase):
        l = frase[i]
        if (frase[i]) in 'bcdfghjklmnpqrstvxwyz':
            l = str.uper(l)
        c = c + 1 
        i += 1
    return c