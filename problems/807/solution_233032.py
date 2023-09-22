def conta_frases(texto):
    """recebe um texto em string e retorna o numeros de frases que contém no texto
    str -> int"""

    texto1 = texto.replace("...", "/")
    texto2 = texto1.replace(".", "/")
    texto3 = texto2.replace("!", "/")
    texto4 = texto3.replace("?", "/")
    
    frases = texto4.split("/")
	
    if frases[-1] == "":
    	del frases[-1]
        
    return len(frases)