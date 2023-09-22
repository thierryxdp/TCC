def uppCons(frase):
    '''Funcao que retorna as consoantes da frase em maisculo'''
    nfrase=''
    i=0
    while i<len(frase):
        if frase[i]in'bcçdfghjklmnpqrstvxwyz':
            nfrase = nfrase + str.upper(frase[i])
        else:
            nfrase=nfrase+frase[i]
        i=i+1
    return nfrase