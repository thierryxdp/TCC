def uppCons(frase):
    
    letras= 'bcdfghjklmnpqrstvxwyz'
    caractere=0
    letra_maiuscula=''
    
    while caractere<len(frase):
        if frase[caractere] in letras:
            letra_maiuscula=letra_maiuscula+frase[caractere].upper()
           
          
        else:
            letra_maiuscula=letra_maiuscula+frase[caractere]
            caractere=caractere+1
    return letra_maiuscula