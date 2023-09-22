def retira_pontuacao(s):
    '''retira a pontuação'''
    out = s.translate(str.maketrans('', '', string.punctuation))
    return out