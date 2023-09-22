def uppCons(frase):
    '''ok'''
    letra=''.join(consoante.upper() if consoante in 'bcdfghjklmnpqrstvwxzç' else consoante for consoante in frase)
    return letra