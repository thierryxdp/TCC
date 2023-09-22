import string
def retira_pontuacao(frase):
    '''retorna uma frase sem pontos e preenchida com espaços
      str -> str'''
    return str.replace(frase, ('!') , ' ' )