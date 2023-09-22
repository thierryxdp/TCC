def retira_pontuacao(frase):
    
    a = str.join(' ', str.split(frase, '.'))
    b = str.join(' ', str.split(a, ','))
    c = str.join(' ', str.split(b, '?'))
    d = str.join(' ', str.split(c, '!'))
    e = str.join(' ', str.split(d, '-'))
    return e

def inverte(frase2):
	minusculo     = frase2.lower().strip()
	sem_pontuacao = retira_pontuacao(frase2)
	separar       = str.split(sem_pontuacao," ")
	inverter      = separar[::-1]
	juntar        = str.join(" ", inverter)

 	return juntar