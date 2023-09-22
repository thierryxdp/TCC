def retira_pontuacao(frase):
    x0 = frase.sprit('!')
    x1 = x0.sprit(',')
    x2 = x1.sprit('.')
    x3 = x2.sprit('?')
    return x3