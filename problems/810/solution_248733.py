def inversao(A):
	minusculo     = A.lower().strip()
	sem_pontuacao = remover(minusculo)
	separar       = str.split(sem_pontuacao," ")
	inverter      = separar[::-1]
	juntar        = str.join(" ", inverter)

	return juntar