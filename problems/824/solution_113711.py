def uppCons(frase):
    '''Funcão que recebe uma frase e retorna suas consoantes em 
    maiusculas.
    str->str'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        caractere = frase[indice]
        if (frase[indice]) in 'bcdfghjklmnpqrstvwxyzç':
            caractere = str.upper(caractere)
        consoante = consoante+caractere
        
        indice+=1
    return consoante