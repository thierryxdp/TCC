def lingua_p(palavra):
    """ """
    string = ''
    
    palavra = str.lower(palavra)
    for letra in palavra:
        if letra in "aeiouáéíóú":
            string = string + letra + 'p' + letra 
        else:
            string = string + letra
            
    return string