def uppCons(frase):
    '''Função que retorna a frase com as consoantes em maiusculo
    str -> str'''
    c = ''
    i = 0
    while i <len(frase):
        l = frase[i]
        if (frase[i]) in 'bcçdfghjklmnpqrstvxwyz':
            l = str.upper(l)
        c = c + l 
        i += 1
    return c