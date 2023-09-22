def retira_pontuacao (frase):
     nf = ''
     nf = frase.replace (',', ' ').replace (';', ' ').replace ('!', ' ').replace ('-', ' ').replace ('.', ' ').replace ('?', ' ')
     return nf


def inverte (frase):
    return str.lower(retira_pontuacao(frase[::-1]))