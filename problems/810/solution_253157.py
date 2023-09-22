def inversafrase(x):
    frase=x
    frase.replace('.',' ')
    frase.replace(',',' ')
    frase.replace(':',' ')
    frase.replace(';',' ')
    frase.replace('—',' ')
    frase.replace('...',' ')
    u=frase.lower()
    y=u.split()
    y.reverse()
    
    
    return ' '.join(y)