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
    return map(str.frase.replace, pontuacoes, [' ']*len(pontuacoes))