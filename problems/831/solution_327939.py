def lingua_p(palavra):
    listaPalavra=list(palavra)
    i=0
    for letra in listaPalavra:
        if letra.lower() in 'aeiou':
        	listaPalavra.insert(i+1, 'p')
        i+=1
    return listaPalavra