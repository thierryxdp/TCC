import re
def retira_pontuacao(frase):
    s = frase
    saida = ''.join([i for i in s if i not in s.punctuation])
    return saida