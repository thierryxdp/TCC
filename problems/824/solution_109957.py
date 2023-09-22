def uppCons(frase):
    maiuscula=''.join(consoante.upper() if consoante in 'bcdfghjklmnpqrstvwxzç' else consoante for consoante in frase)
    return maiuscula