def conta_frases(frase):
   if frase.replace('...','.'):
    return len(frase.split('.'))
   if frase.replace('?','.'):
    return len(frase.split('.'))
   if frase.replace('!','.'):
    return len(frase.split('.'))