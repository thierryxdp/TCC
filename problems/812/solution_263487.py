def retira_pontuacao(x):
    '''retira a pontuação presente em uma frase'''
    frase=0
    if '-' in x:
        frase=+frase+split('-')
    if ',' in x:
        frase=+frase+split(',')
    if ':' in x:
        frase=+frase+split(':')
    if ';' in x:
        frase=+frase+split(';')
    if '?' in x:
        frase=+frase+split('?')
    if '!' in x:
        frase=+frase+split('!')