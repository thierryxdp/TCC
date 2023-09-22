def conta_frases(texto):
    """
    	Função que conta o número de frases que aparecem no texto 
        dado.
   		string -> int 
    """
    texto1 = texto.split('?')
    texto2 = texto.split('!')
    texto3 = texto.split('!')
    texto4 = texto1+texto2+texto3
    return texto4