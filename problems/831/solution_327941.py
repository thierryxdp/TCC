def lingua_p(palavra):
    listaPalavra=list(palavra)
    listaAux=[]
    i=0
    for letra in listaPalavra:
        if letra.lower() in 'aeiou':
            listaAux.append(letra)
            listaAux.append('p')
        	#listaPalavra.insert(i+1, 'p')
        else:
            listaAux.append(letra)
        i+=1
    return listaAux