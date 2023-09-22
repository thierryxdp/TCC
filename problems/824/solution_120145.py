def uppCons(frase):
    '''funcao que retorna todas as letras consoantes de uma frase como letras maiusculas str->str'''
    i = 0
    
    texto = ''
    
    while i < len(frase):
        
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            
            texto = texto + str.upper(frase[i])
            
        else:
            
            texto = texto + frase[i]
            
        i = i + 1
        
    return frase