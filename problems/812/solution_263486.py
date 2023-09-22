def retira_pontuacao(x):
    '''retira a pontuação presente em uma frase'''
    frase=0
    if '-' in x:
        frases=+frases+split('-')
    if ',' in x:
        frases=+frases+split(',')
    if ':' in x:
        frases=+frases+split(':')
    if ';' in x:
        frases=+frases+split(';')
    if '?' in x:
        frases=+frases+split('?')
    if '!' in x:
        frases=+frases+split('!')