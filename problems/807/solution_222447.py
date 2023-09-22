def conta_frases(texto):
    
    str.replace(texto,"!",".")
    str.replace(texto,"?",".")

    
    
    listaTexto = str.split(texto, ".")
	return len(listaTexto)