conta_frases(frase):
    s=frase
    f1=s.split('. ')
    f2=s.split('? ')
    f3=s.split('... ')
    f4=s.split('! ')
    return f1+f2+f3+f4