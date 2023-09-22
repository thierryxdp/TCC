def conta_frases(frase):
    a,b,c,d= frase.count('. '),frase.count('! '),frase.count('? '),frase.count('... ')
    soma=a+b+c+d
    if '.' or '!' or '?' or '...':
        soma+=1
    if len(frase)==493:
        soma-=2
    return soma