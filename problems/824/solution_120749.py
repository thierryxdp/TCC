def uppCons1(frase):
    return ''.join(c.upper() if c in 'bcdfghjklmnpqrstvxwyzç' else c for c in frase)