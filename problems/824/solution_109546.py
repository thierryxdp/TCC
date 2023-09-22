def uppCons(frase):
    """Função que recebe como entrada uma frase e retorna esta com todas as suas 
    consoantes em maiúsculas e os demais caracteres exatamente como estavam na
    frase original 
    
        Parameters:
        frase: uma string que contem a frase a ser alterada 
        
        Returns:
        Retorna a frase de entrada contendo todas as consoantes maiúsculas e
        as vogais da mesma forma que estavam na frase original, dado que:
        str -> str."""
    frase_tratada= ''
    for caractere in frase:
        if caractere in 'çbcdfghjklmnpqrstvxwyz':
            caractere=str.upper(caractere)
        frase_tratada=frase_tratada + caractere
    return frase_tratada