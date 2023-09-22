def inverte(frase):
    """Inverte uma frase e retira as pontuações
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
    
    separar = str.split(texto, " ")
    inverter = separar[::-1]
    frase_invertida = str.join(" ", inverter)
    
    return frase_invertida