def retira_pontuacao (frase):
    return ''.join([i for i in frase if i not in frase.punctuation])