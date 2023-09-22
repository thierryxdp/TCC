def verificaCaracter(c):
    
    pontuacoes = [
        '-',
        '...',
        '.',
        ';',
        '!'
        '?',
        ',',
        ':'
    	]
    return ' ' if c in pontuacoes else c

def retira_pontuacao(frase):
    'Remove todas as pontuacoes da frase'
    
    fraseAlterada = str.join(
    	'',
    	map(verificaCaracter,frase)
    	)
    return fraseAlterada