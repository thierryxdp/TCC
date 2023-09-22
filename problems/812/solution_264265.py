def retira_pontuacao(A):
    A        = str(A)
    remocao1 = A.translate(str.maketrans('.'," "))
    remocao2 = remocao1.translate(str.maketrans('!'," "))
	remocao3 = remocao2.translate(str.maketrans('?'," "))

	return remocao3