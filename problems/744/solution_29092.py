def hashtag(s):
    # Recebe a string, divide na metade, insere uma hashtag no início, meio e fim, devolve a nova string.
    # str-> str
    tamanho=len(s)
    if (tamanho%2) == 0:
        return "#"+s[:tamanho/2]+"#"+s[tamanho/2:]+"#"
    
    else:
    	return "#"+s[:(tamanho-1)/2]+"#"+s[(tamanho-1)/2:]+"#"