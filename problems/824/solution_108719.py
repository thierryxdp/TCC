def uppCons(frase):
    '''descricao'''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            consoantes=consoantes+frase[i]
        i=i+1
    return str.upper(consoantes)