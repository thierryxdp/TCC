def inverte(frase):
    """Função que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.
    
    	Parameters:
        frase: frase que será alterada (str)
        
        Returns: frase com as alterações solicitadas (str)
    """

    for pontuacao in ".!?-,:;":

        frase = frase.replace(pontuacao, " ")

		frase = str.split(frase, " ")
        
        frase = frase.reverse()
        
        frase = str.join(" ", frase)

	return frase