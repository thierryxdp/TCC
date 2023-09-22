def conta_frases(texto):
    """
    	Função que conta o número de frases que aparecem no texto 
        dado.
   		string -> int 
    """
    texto = texto.split('?')+texto.split('!')
    return len(texto)