def uppCons(frase: str) -> str:
    """ Retorna a frase fornecida, mas com todas as suas 
    consoantes em maiúsculas. """
    
    i = 0
    
    while (i < len(frase)):
        if (min(frase[i]) not in 'aeiouàáâãóôõéêíú'):
            frase = str.replace(frase,frase[i],str.upper(frase[i]))
        i += 1
        
    return frase