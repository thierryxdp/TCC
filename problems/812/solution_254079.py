def retira_pontuação(frase):
   """  Faca uma funcao que dada uma frase, substitua todos os espacos em branco por '#',
   so que sem usar a funcao replace."""
    
    frase = str.split(frase, " ")
    frase = str.join("#", frase)
    return frase