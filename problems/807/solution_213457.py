def conta_frases (frase):
   a = frase.replace ('...', '@')
    return a.count('.') + a.count('!') + a.count('?') + a.count('@')