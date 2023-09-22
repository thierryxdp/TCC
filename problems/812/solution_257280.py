def retira_pontuacao(frase):
    if "!" in frase:
        return str.replace(frase,"!"," ")
    elif "." in frase:
        a=str.replace(frase,"."," ")
    	return str.split(a)
        if "," in frase:
        	return str.replace(frase,","," ")  
    elif ":" in frase:
        return str.replace(frase,":"," ")
    elif "," in frase:
        a=str.replace(frase,","," ")
        return a
    	if "?" in a:
        	return str.replace(a,"?","  ")
    elif "?" in frase:
        return str.replace(frase,"?"," ")
    #elif "," and "?" in frase:
     #   return str.replace(frase,",",?",'')
    elif "-" in frase:
        return str.replace(frase,"-"," ")