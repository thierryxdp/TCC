def retira_pontuacao(frase):
    frase=frase.split('.')
    frase=frase.split(',')
    frase=frase.split(';')
    frase=frase.split(':')
    frase=frase.split('-')
    frase=' '.join(frase)
    return frase