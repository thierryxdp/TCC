def mediaDaTurma(listaNotasAlunos):
    somaLista = sum(listaNotasAlunos)
    mediaDaTurma = somaLista/len(listaNotasAlunos)
    if n not in lista:
        listaSomada = lista + [n]
        listaSomada.sort()
        maioresQ = listaSomada[listaSomada.index(n)+1:]
        return maioresQ
    else:
        lista.sort()
        maioresQ = lista[lista.index(n)+1:]
        return maioresQ
    notasAcimaDaMedia = maiores(listaNotasAlunos,mediaDaTurma)
    return (mediaDaTurma,notasAcimaDaMedia)