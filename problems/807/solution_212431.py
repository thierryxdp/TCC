def conta_frases(frase):
    """Calcula e retorna a quantidade de frases dada um string;
    str->int"""
    a,b,c,d= frase.count('.'),frase.count('!'),frase.count('?'),frase.count('...')*(-2)
    soma=a+b+c+d
    return soma