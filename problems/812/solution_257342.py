def retira_pontuacao(x):
    y = (str.replace(x, '-',' ') + str.replace(x, ',',' ') + str.replace(x, ':',' '))
    return y