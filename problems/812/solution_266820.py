def retira_pontuacao(pal):
    d = { '.': ' ', ':' : ' ', ';' : ' ', '-' : ' ', ',' : ' ', '?' : ' ', '!' : ' '}
    for x in d:
        pal =  str.replace(pal, x, d[x])
    return pal