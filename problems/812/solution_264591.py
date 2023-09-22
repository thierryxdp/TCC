def retira_pontuacao(frase):
    for i in ['-', ',', ':', ';', '.']:
      frase.replace(i, ' ')
    return frase