def lingua_p(palavra):
    """Retorna uma palavra traduzida para língua do p
    	str -> str
        Parameters:
        palavra: Palavra em português
        
        Returns:
        Palavra traduzida para língua do p
    """
    palavra = str.lower(palavra)
    traducao = ''
    vogais = 'aeiouãáâéíóúõô'
    
    for i in palavra:
        traducao = traducao + i
        if i in vogais:
            traducao = traducao + 'p' + i
            
    return traducao