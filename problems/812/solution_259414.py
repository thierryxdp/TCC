def verifica_pont(c):
    ''' verifica as pontuações presentes na frase'''
    pontuacoes = ['-', '...', '.', ',', '!', '?']
    return ' ' if c in pontuacoes else c

def retira_pontuacao(frase):
    ''' retira a pontuação'''
    fraseNew = str.join(' ',list(map(verifica_pont, frase)))
    
    return fraseNew