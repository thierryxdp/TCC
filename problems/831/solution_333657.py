# a funçao recebe uma palavra e a cada vogal é adicionada um p mais uma vogal
def lingua_p(palavra):
	traduzido_p = []
	contador = 0
	for letra in list(palavra):
		if letra in ’aeiou´a´e´ı´o´u’:
			traduzido_p.append(letra + ’p’ + letra)
		else:
			traduzido_p.append(letra)
	return ’’.join(traduzido_p)