def conta_frases(frase):
    n_frases = 0
    n_frases += len(frase.split('.'))
    n_frases -= (len(frase.split('...')) - 1) * 3
    n_frases += len(frase.split('!')) - 1
    n_frases += len(frase.split('?')) - 1
    return n_frases