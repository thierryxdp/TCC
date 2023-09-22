def uppCons(frase):
    
    s = ''
    caractere=0
    while caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s= caractere.upper()
            
            caractere=caractere+1
        else:
            s= caractere
    return s