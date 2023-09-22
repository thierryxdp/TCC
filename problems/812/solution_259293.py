def retira_pontuacao(frase):
    'Remove todas as pontuacoes da frase'
    pontuacoes = [
        '--',
        '...',
        '.',
        ';',
        '!',
        '?',
        ',',
        ':'
    	]
    return list(map(str.replace, [frase]*len(pontuacoes), pontuacoes, [' ']*len(pontuacoes)))