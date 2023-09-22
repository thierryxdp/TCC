def mediaDaTurma(listaNotasAlunos):
    somaLista = sum(listaNotasAlunos)
    mediaDaTurma = somaLista/len(listaNotasAlunos)
    notasAcimaDaMedia = maiores(listaNotasAlunos,mediaDaTurma)
    return (notasAcimaDaMedia)