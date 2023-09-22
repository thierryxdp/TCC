def inverte(frase):
    """Inverte uma frase e retira as pontuações
    	str -> str
    	Parameters:
        frase: Frase que se deseja inverter
        
        Returns:
        Frase invertida e sem pontuações
     """
    
    frase = frase.replace('...',' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('-',' ')
    frase = str.lower(frase)
    
    separar = str.split(frase, " ")
    inverter = separar[::-1]
    frase_invertida = str.join(" ", inverter)
    frase_invertida = [1::]
    
    return frase_invertida