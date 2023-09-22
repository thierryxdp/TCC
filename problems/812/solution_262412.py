def retira_pontuacao(frase):
    'Funcao que dada um frase, substitui a pontuacao por espaco'
    'str=>str'
    frase=frase.replace(':',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('/',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('!',' ')
    return frase