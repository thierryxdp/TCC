def lingua_p(palavra):
    """ 
    	Funcao que retorna um palavra traduzina para a lingua do P;
    	str -> str
    """
    vogal = 'aeiouáéíóúâãêẽîĩôõûũàèìòù'
    nova_palavra = ''
    for letra in palavra.lower():
        if letra in vogal:
            nova_palavra += letra + 'p' + letra
        else:
            nova_palavra += letra
            
    return nova_palavra