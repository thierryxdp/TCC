def acima_da_media(listaNotasAlunos):
    somaLista = sum(listaNotasAlunos)
    mediaDaTurma = somaLista/len(listaNotasAlunos)
    def maiores(lista,n):
    	if n not in lista:
        	listaSomada = lista + [n]
        	listaSomada.sort()
       		maioresQ = listaSomada[listaSomada.index(n)+1:]
    	else:
        	lista.sort()
        	maioresQ = lista[lista.index(n)+1:]
    notasAcimaDaMedia = maiores(listaNotasAlunos,mediaDaTurma)
    return (notasAcimaDaMedia)