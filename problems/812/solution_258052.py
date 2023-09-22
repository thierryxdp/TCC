def retira_pontuacao(frase):
    while frase.find('-'):
        return frase.replace('-',' ')
    while frase.find('!'):
        return frase.replace('!',' ')