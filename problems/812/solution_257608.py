def retira_pontuacao(frase):
    
    lista = ['-' , ',' , ':' , ';' , '.' , '!' , '?']

    
    
    if "!" in frase:
    	return str.replace(frase,"!"," ")
    
    elif "?" in frase:
        return str.replace(frase,"?"," ")
    
    elif "." in frase:
        return str.replace(frase,"."," ")
    
    elif ":" in frase:
        return str.replace(frase,":"," ")
    
    elif "," in frase:
        return str.replace(frase,","," ")
    
    elif ";" in frase:
        return str.replace(frase,";"," ")
    
    elif "-" in frase:
        return str.replace(frase,"-"," ")
    
    else:
        return frase