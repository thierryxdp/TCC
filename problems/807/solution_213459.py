def conta_frases (frase):
   frase1 = str.replace (frase,'...', '@')
    return frase1.count('.') + frase1.count('!') + frase1.count('?') + frase1.count('@')