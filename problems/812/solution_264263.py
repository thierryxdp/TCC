def retira_pontuacao(A):
    
	remocao1 = A.translate(str.maketrans('.'," "))
	remocao2 = remocao1.translate(str.maketrans('!'," "))
	remocao3 = remocao2.translate(str.maketrans('?'," "))
	remocao4 = remocao3.translate(str.maketrans(','," "))    

	return remocao4