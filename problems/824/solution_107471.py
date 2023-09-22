#QUESTÃO2
def uppCons(frase):
    '''
    A função retorna todas as consoantes
    em maiusculo.
    list -> string
    '''
    i = 0
    fraseAlt = ''
    while i < len(frase[0]):
        if frase[0][i] in 'bcdfghjklmnpqrstvxwyz':
            fraseAlt = fraseAlt + (frase[0][i].upper())
        else:
            fraseAlt = fraseAlt + frase[0][i]
    	i = i+1
    return fraseAlt