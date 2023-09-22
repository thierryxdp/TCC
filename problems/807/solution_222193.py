def conta_frases(texto):
    """
    	Função que conta o número de frases que aparecem no texto 
        dado.
   		string -> int 
    """
    x = a or e or i or o or u or r or s
    texto = texto.split('?')+texto.split('!')+texto.split(x'.')
    return len(texto)