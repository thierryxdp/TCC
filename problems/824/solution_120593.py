def uppCons(frase):
    string = ''
    for x in frase:
        if x in 'bcçdfghjklmnpqrstvwxyz':
            string+=x.upper()
        else:
            string+=x
    return string