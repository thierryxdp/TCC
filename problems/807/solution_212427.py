def conta_frases(frase):
    a,b,c,d= frase.count('.'),frase.count('!'),frase.count('?'),frase.count('...')*(-2)
    soma=a+b+c+d
    return soma