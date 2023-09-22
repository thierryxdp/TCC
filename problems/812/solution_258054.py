def retira_pontuacao(frase):
    if frase.find('!'):
        return frase.replace('!',' ')