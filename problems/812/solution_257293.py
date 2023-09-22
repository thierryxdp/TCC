def retira_pontuação(frase):
    """Mostra a frase fornecida sem pontuações
    	str -> str
    	Parameters:
        frase: Frase a ser analisada
        
        Returns:
        Frase com as pontuações substituídas por espaços
    """
    
    frase = frase.replace('...',' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(',',' ')
    
    return frase