def acima_da_media(listaNotasAlunos):
    n = 7
    if n not in listaNotasAlunos:
        listaSomada = listaNotasAlunos + [n]
        listaSomada.sort()
        maioresQ = listaSomada[listaSomada.index(n)+1:]
    else:
        listaNotasAlunos.sort()
        maioresQ = lista[lista.index(n)+1:]
        
	somaLista = sum(listaNotasAlunos)
    x = somaLista/len(listaNotasAlunos)
    y = maiores(listaNotasAlunos,x)
    return (x,y)