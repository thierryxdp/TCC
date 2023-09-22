def lingua_p(p):
    '''---'''
    
    frase = ' '
    
    for letra in palavra:
        if str.lower(letra) in "aàâãeéêiíoóõôuúũ":           
        	frase += letra + "p" + letra
        else:
            frase += letra
            
    return frase