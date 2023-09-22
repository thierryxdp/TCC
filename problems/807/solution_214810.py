#conta o numero de frases que aparecem no texto
def conta_frases(frases):
	'retorna a quantidade de frases no texto'
	string_pontuada = frases.replace('!','.')
	string_pontuada = string_pontuada.replace('?','.')
	string_pontuada = string_pontuada.replace('!','.')
	string_pontuada = string_pontuada.replace('...','.')
    return string_pontuada.count('.')