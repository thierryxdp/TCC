def retira_pontuacao(F):
    x0 = F.strip('!')
    x1 = x0.strip(',')
    x2 = x1.strip('.')
    x3 = x2.strip('?')
    return str(x3) + str(" ")