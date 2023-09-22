def retira_pontuacao(x):
    '''função que retira pontuação do texto'''
    return x.replace('-',' ') and or x.replace(',',' ') and or x.replace(':', ' ') and or x.replace(';', ' ') and or x.replace ('?', ' ') and or x.replace('!', ' ') and or x.replace('.', ' ')