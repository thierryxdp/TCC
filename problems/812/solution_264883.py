def retira_pontuacao(frase):
    '''retorna uma frase sem pontos e preenchida com espaços
      str -> str'''
    for string.punctuation in frase
    frase = frase.replace(string.punctuation,"")
    return frase