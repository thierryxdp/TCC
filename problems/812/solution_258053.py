def retira_pontuacao(frase):
    while frase.find('-'):
        return frase.replace('-',' ')
    if frase.find('!'):
        return frase.replace('!',' ')