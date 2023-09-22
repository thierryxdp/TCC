def conta_frases(texto):
    """ Dado um texto conta a quantidade de frases presentes do noesmo.
    	entrada string -> saida inteiro."""
  
    frases = texto.split("!")
    frases = texto.split("?")
    frases = texto.split(".")
    frases = texto.split("...")
    
    
    return len(frases)