def retira_pontuacao(x):
    '''retira a pontuação presente em uma frase'''
    frase=0
    if '-' in x:
        frase=+x.split('-')
    if ',' in x:
        frase=+x.split(',')
    if ':' in x:
        frase=+x.split(':')
    if ';' in x:
        frase=+x.split(';')
    if '?' in x:
        frase=+x.split('?')
    if '!' in x:
        frase=+x.split('!')
     
    
    return frase