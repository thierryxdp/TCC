def acima_da_media(listaNotasAlunos):
    somaLista = sum(listaNotasAlunos)
    mediaDaTurma = somaLista/len(listaNotasAlunos)
    def maiores(lista,7):
    	if 7 not in lista:
        	listaSomada = lista + [7]
        	listaSomada.sort()
       		maioresQ = listaSomada[listaSomada.index(7)+1:]
    	else:
        	lista.sort()
        	maioresQ = lista[lista.index(7)+1:]
    notasAcimaDaMedia = maiores(listaNotasAlunos,mediaDaTurma)
    return (notasAcimaDaMedia)