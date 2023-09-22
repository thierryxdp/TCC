def retira_pontuacao(frase):
    frasee = (-,:;.)
    return ''.join(i if i not in frasee else ' ' for i in frase)