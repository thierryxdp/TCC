def uppCons(frase):
    
    '''Função que retorna as consoantes de uma
    frase em maiúsculas.
    
    :param frase:str
    return:str'''
    
    letras= 'bcdfghjklmnpqrstvxwyz'
    caractere=0
    letra_maiuscula=''
    
    while caractere<len(frase):
        if frase[caractere] in letras:
            return letra_maiuscula=letra_maiuscula+frase[caractere].upper()
           
          
        else:
            letra_maiuscula=letra_maiuscula+frase[caractere]
            caractere=caractere+1
    return letra_maiuscula