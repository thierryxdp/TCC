acima_da_media(listaAluno):
    media = sum(listaAluno)/len(listaAluno)
    lista = []
	for i in range(len(listaAluno)):
        if listaAluno[i] > media:
            lista.append(listaAluno[i])
    lista = sorted(lista)
    
    return lista