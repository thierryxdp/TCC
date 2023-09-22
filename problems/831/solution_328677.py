def lingua_p(palavra):
    '''Função que retorna um string alterada da "palavra" de entrada: str-> str'''
    
    palavra_alterada = ''
    
    for letra in palavra:
        if str.lower(letra) in "aáàâãeéêiíoóõôuúũ":           
        	palavra_alterada += letra + "p" + letra
        else:
            palavra_alterada += letra
            
    return palavra_alterada