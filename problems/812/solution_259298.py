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
    resultado = [frase]
    return list(map(
        lambda l, old, new: str.replace(l[0],old, new), [resultado]*len(pontuacoes),
		pontuacoes, 
		[' ']*len(pontuacoes)
		))[-1]