def uppCons(frase):
    '''ok'''
    letra=''.join(consoante.upper() if consoante in 'bcdfghjklmnpqrstvwxzç' else frase)
    return letra