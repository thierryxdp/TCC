def verificaCaracter(c):
    "Verifica se o caracter é uma pontuacao, caso seja return ' ',caso nao seja retorna o mesmo caracter"
    pontuacoes = [
        '--',
        '...',
        '.',
        ';',
        ':',
        '!',
        ',',
        '-',
        '?'
    	] 
    return ' ' if c in pontuacoes else c

def retira_pontuacao(frase):
    "Retorna a frase com as pontuações retiradas"
    fraseAlterada = str.join(
        '',
        map(verificaCaracter,frase)
    	)
    return fraseAlterada