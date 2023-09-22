import re
def retira_pontuacao(frase):
    s = frase
    saida = ''.join([not in s.punctuation])
    return saida