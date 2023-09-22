def retira_pontuacao(frase):
    frase = set('-,:;.')
    return ''.join(i if i not in frase else ' ' for i in frase)