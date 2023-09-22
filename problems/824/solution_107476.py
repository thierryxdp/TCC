#QUESTÃO2
def uppCons(frase):
    '''
    A função retorna todas as consoantes
    em maiusculo.
    string -> string
    '''
    i = 0
    fraseAlt = ''
    while i < len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvxwyz':
            fraseAlt = fraseAlt + (frase[i].upper())
        else:
            fraseAlt = fraseAlt + frase[i]
    	i = i+1
    return fraseAlt