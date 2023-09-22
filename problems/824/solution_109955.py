def uppCons(frase):
    maiuscula=''.join(consoante.upper() if consoante in 'bcdfghjklmnpqrstvwxz' else consoante for consoante in frase)
    return maiuscula