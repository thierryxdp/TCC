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
    return map(str.replace, [frase]*len(pontuacoes), pontuacoes, [' ']*len(pontuacoes))