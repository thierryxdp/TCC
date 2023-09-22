def retira_pontuacao(frase):
    'substitui as pontuacoes por espacos; str -> str'''
    pontuacoes = [
        '-'
        '...'
        '.'
        '!'
        '?'
        ';'
        ':'
        ','
    ]
    return map(str.frase.replace, pontuacoes, [' ']*len(pontuacoes))