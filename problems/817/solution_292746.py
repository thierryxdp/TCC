def mediaDaTurma(listaNotasAlunos):
    if n not in lista:
        listaSomada = lista + [n]
        listaSomada.sort()
        maioresQ = listaSomada[listaSomada.index(n)+1:]
    else:
        lista.sort()
        maioresQ = lista[lista.index(n)+1:]
    somaLista = sum(listaNotasAlunos)
    mediaDaTurma = somaLista/len(listaNotasAlunos)
        notasAcimaDaMedia = maiores(listaNotasAlunos,mediaDaTurma)
    return (mediaDaTurma,notasAcimaDaMedia)