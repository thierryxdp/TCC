def consoantes_maiusculas(frase):
   """dada as entradas retoranar a frase com tdas as suas consoantes em maiusculo"""
   def consoantes_maiusculas(frase):
    maiscula = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper()
        else:
            s += caractere
    return s