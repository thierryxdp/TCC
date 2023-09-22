def retira_pontuacao (x):
    s = ''
    if "," in x:
        return s = s + str.replace(x,","," ",str.count(x,","))