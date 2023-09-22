def retira_pontuacao(x):
    '''função que retira pontuação do texto'''
    return x.replace('-',' ') and x.replace(',',' ') and x.replace(':', ' ') and x.replace(';', ' ') and x.replace ('?', ' ') and x.replace('!', ' ') and x.replace('.', ' ')