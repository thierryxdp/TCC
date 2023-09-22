def conta_frases(frase):
   """função que retorna a quantidade de frases
   str -> str"""
   if ' . . . ' in frase:
        ' . . . ' == 1 
   return str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'.') + str.count(frase,' . . . ')