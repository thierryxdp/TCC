def inverte(frase):
    """Função que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.
    
    	Parameters:
        frase: frase que será alterada (str)
        
        Returns: frase com as alterações solicitadas (str)
    """

    for pontuação in ".!?-,:;":


        frase1 = frase.replace(pontuação, " ")

		frase2 = str.split(frase1, " ")
        
        frase3 = frase2.reverse()
        
        frase4 = str.join(" ", frase3)