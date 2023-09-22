def uppCons(frase):
    i=0
    maiscula = ''
    while i<len(frase):
        if frase[i]in 'bcçdfghjklmnpqrstvxwyz':
            maiscula= maiscula + str.upper(frase[i])
        else:
            maiscula= maiscula +frase[i]
        i=i+1
    return maiscula