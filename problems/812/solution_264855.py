def retira_pontuacao(frase):
    '''retorna uma frase sem pontos e preenchida com espaços
      str -> str'''
    return frase.translate(str.maketrans('', '', string.punctuation))