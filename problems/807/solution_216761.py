def conta_frases(frase):
    s=frase
    f1=len(s.split('.'))
    f2=len(s.split('?'))
    f3=len(s.split('...'))
    f4=len(s.split(' ! '))
    return f1+f2+f3+f4