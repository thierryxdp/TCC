def retira_pontuacao(frase):
    fraseF = frase.split('-')
    fraseF = frase.split(',')
    fraseF = frase.split(':')
    fraseF = frase.split(';')
    fraseF = frase.split('.')
    return ''.join(fraseF)