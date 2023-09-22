def retira_pontuacao(frase):
	x = str.count(frase, '/')
	x += str.count(frase, ',')
	x += str.count(frase, ':')
	x += str.count(frase, ';')
    x += str.count(frase, '.')
    
    return str.replace(frase, '/' and ',' and ':' and ';' and '.', ' ', x)