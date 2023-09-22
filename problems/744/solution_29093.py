def hashtag(s):
    # Recebe a string, divide na metade, insere uma hashtag no início, meio e fim, devolve a nova string.
    # str-> str
    tamanho=len(s)
    if (tamanho%2) == 0:
        meio=tamanho/2
        return "#"+s[:meio]+"#"+s[meio:]+"#"
    
    else:
        meio=(tamanho-1)/2
    	return "#"+s[:meio]+"#"+s[meio:]+"#"