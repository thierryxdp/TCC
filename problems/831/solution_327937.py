def lingua_p(palavra):
    listaPalavra=list(palavra)
    i=0
    for letra in listaPalavra:
        if letra.lower()=='aeiou':
            return listaPalavra
        	listaPalavra.insert(i+1, 'p')
            i+=1