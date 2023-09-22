def retira_pontuacao(frase):
    for i in ('.?:;_,!'):
        frase = frase.replace(i,' ')
    return frase