def lingua_p(palavra):
    listaPalavra=str.split(palavra)
    i=0
    for letra in range(len(listaPalavra)):
        if letra.lower()=='aeiou':
        	listaPalavra.insert(i+1, 'p')
       	i+=1
    return listaPalavra