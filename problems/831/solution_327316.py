def lingua_p(palavra):
    """Traduz a palavra para a lingua do p
       string --> string"""
    vogais = ("aeiou")
    newPalavra = []
    
	for i in palavra:
        if i in vogais:
    	    newPalavra.append(i + "p" + i)
        else:
            newPalavra.append(i)
    return str.join(newPalavra)