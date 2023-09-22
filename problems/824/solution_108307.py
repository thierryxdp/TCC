def uppCons(frase):
    '''funçao que dada uma frase retorna todas consoantes em maiusculo'''
    i = 0
    cons = ' '
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frasenova = frase.upper(frase[i])
            i = i+1
            return frasenova