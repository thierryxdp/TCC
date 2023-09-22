def conta_frases(frase):
     
     frase.replace('!','.',1)
     frase.replace('?','.',1)
     
     return len (frase.split('.'))