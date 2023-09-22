def conta_frases (frase):
   frase1 = frase.replace ('...', '@')
    return frase1.count('.') + frase1.count('!') + frase1.count('?') + frase1.count('@')