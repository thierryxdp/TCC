def mediaDaTurma(listaNotasAlunos):
	somaLista = sum(listaNotasAlunos)
    x = somaLista/len(listaNotasAlunos)
    y = maiores(listaNotasAlunos,x)
    return (x,y)