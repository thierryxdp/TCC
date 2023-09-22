def conta_frases(frase):
    """Funçao que me dada uma frase, me retorna a quantidade de quantas frases que são terminadas com pontuações.
E isso me retorna quantas frases, estão dentro desta mesma frase. str>int"""
    A=str.count(frase,'?')
    B=str.count(frase,'...')
    C=str.count(frase,'!')
    D=str.count(frase,'. ')
    E=str.count(frase,'.')
    F=str.count(frase,(',')
    if E==frase[-1]:
        return D+C+A+B+E
    
    else:
        return (D+C+A+B)