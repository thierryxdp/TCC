def consoantes_maiusculas(frase):
   """dada as entradas retoranar a frase com tdas as suas consoantes em maiusculo"""
   return ''.join(caractere.upper() if carc in 'bcdfghjklmnpqrstvxwyz'
                   else caractere for caractere in frase)