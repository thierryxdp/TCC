def uppCons(frase):
    '''descricao'''
    i=0
    consoantes=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            consoantes=consoantes+texto[i]
        i=i+1
    return str.upper(consoantes)