def verificaCaracter(c):
    "Remove todas as pontuacoes da frase"
    pontuacoes = [
        '--',
        '...',
        '.',
        ';',
        ':',
        '!',
        ',',
    	] 
    return ' ' if c in pontucoes else c

def retira_pontuacao(frase):
    fraseAlterada = str.join(
        '',
        map(verificaCaracter,frase)
    	)
    return fraseAlterada