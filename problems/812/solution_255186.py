def retira_pontuacao(x, y):
    novastring = x
    for x in y:
        novastring = novastring.replace(x, '')
    return novastring