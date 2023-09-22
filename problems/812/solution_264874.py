import string
def retira_pontuacao(frase):
    '''retorna uma frase sem pontos e preenchida com espaços
      str -> str'''
    varia = str('.' and '?' and '!' and ',' and '-')
    return str.replace(frase, (varia)  , ' ' )