def verificaCaracter(c):
    '''substitui as pontuacoes por espacos; str -> str'''
    pontuacoes = [
        '-',
        '...',
        '.',
        '!',
        '?',
        ';',
        ':',
        ',',
    	]
    return ' ' if c in pontuacoes else c

def retira_pontuacao(frase):
    '''retira pontuacao da frase; str -> str'''
    fraseAlterada = str.join(
        '',
        map(verificaCaracter,frase))
    return fraseAlterada