def conta_frases(texto):
   return len(texto.split('? ') or texto.split('... ') or texto.split('. ') or texto.split('? '))