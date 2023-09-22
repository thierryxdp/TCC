def inverte(x):
    frase=x
    frase = frase.replace('.',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('—',' ')
    frase = frase.replace('...',' ')
    u=frase.lower()
    y=u.split()
    y.reverse()
    
    return ' '.join(y)