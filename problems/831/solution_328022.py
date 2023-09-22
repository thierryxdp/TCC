def lingua_p(palavra: str)-> str:
    """ Traduz uma palavra da língua portuguesa para a língua do P."""
    
    palavra = str.lower(palavra)
    letras = list(palavra)
    i = 1
    
    while(i - 1 < len(letras)):
        if (letras[i - 1] in 'aeiouáàâãéêíóôõú'):
            list.insert(letras, i ,'p' + letras[i - 1])
            i += 2
        i += 1
        
    return str.join('',letras)