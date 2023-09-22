def conta_frases(frase):
    """Funçao que me dada uma frase, me retorna a quantidade de quantas frases que são terminadas com pontuações.
E isso me retorna quantas frases, estão dentro desta mesma frase. str>int"""
    A=frase.count('. ')
    B=frase.count('.')
    C=frase.count('!')
    D=frase.count('?')
    E=frase.count('...')
    if B==frase[-1]:
        return A+B+C+D+E
    else: 
        return (A+C+D+E)