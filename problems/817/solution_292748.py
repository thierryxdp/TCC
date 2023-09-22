def mediaDaTurma(listaNotasAlunos):
	somaLista = sum(listaNotasAlunos)
    x = somaLista/len(listaNotasAlunos)
    notasAcimaDaMedia = maiores(listaNotasAlunos,x)
    return (x,notasAcimaDaMedia)