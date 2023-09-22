def lingua_p(palavra):
    listaPalavra=str.split(palavra)
    i=0
    for letra in listaPalavra:
        return letra
        if letra.lower() in 'aeiou':
        	listaPalavra.insert(i+1, 'p')
            i+=1
    return listaPalavra