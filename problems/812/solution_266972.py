def retira_pontuacao (x) :
    out = ''.join([i for i in x if i not in str.punctuation])
    return out