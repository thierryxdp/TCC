def retira_pontuacao(frase):
    
    lista = ('-' , ',' , ':' , ';' , '.' , '!' , '?')

    travessao = str.find(frase,"-")
    virgula = str.find(frase,",")
    doispontos = str.find(frase,":")
    pontovirgula = str.find(frase,";")
    ponto = str.find(frase,".")
    exclamacao = str.find(frase,"!")
    interrogacao = str.find(frase,"?")
    
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