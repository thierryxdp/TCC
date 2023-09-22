def conta_frases(frase):
    """Funçao que me dada uma frase, me retorna a quantidade de quantas frases que são terminadas com pontuações.
E isso me retorna quantas frases, estão dentro desta mesma frase. str>int"""
    return frase.count('.')+frase.count('!')+frase.count('?')-frase.count('...')+frase.count(' ')