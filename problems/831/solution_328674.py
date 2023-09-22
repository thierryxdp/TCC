def lingua_p(palavra):
    '''---'''
    
    palavra_alterada = ' '
    
    for letra in palavra:
        if str.lower(letra) in "aàâãeéêiíoóõôuúũ":           
        	palavra_alterada += letra + "p" + letra
        else:
            palavra_alterada += letra
            
    return palavra_alterada