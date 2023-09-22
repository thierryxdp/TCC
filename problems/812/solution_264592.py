def retira_pontuacao(frase):
    caract = ['-', ',', ':', ';', '.', '?', '!']
    for i in caract:
      frase = frase.replace(i, ' ')
    return frase