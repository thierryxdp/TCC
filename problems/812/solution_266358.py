def retira_pontuacao(x):
    if '-' in x:
        x= str.replace(x, '-', ' ')