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
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            fraseAlt = fraseAlt + (frase[i].upper())
        else:
            fraseAlt = fraseAlt + frase[i]
    	i = i+1
    return fraseAlt