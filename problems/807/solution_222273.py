def conta_frases(texto):
    """
    	Função que conta o número de frases que aparecem no texto 
        dado.
   		string -> int 
    """
    texto1 = texto.count('?')
    texto2 = texto.count('!')
    texto3 = texto.count('. ')
    texto4 = texto.count('...')
    return texto1+texto2+texto3+texto4