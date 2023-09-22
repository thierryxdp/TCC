def uppCons(frase):
    """Retorna a frase recebida com todas as suas consoantes maiúsculas
    	str -> str
        Parameters:
        frase: Frase a ser modificada
        
        Returns:
        A frase com todas as consoantes maiúsculas
    """
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    i = 0
    
    while i<len(frase):
        if frase[i] not in vogais:
            frase = frase.replace(frase[i],frase[i].upper)
		i = i+1
    return frase