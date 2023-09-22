def uppCons(frase):
    '''funcao que retorna todas as consoantes de uma frase
    maiúscula; str -> str'''
    
    b= frase
    i = 0
      
    while i < len(frase):
        
        if frase[i] in 'bcdfghjklmnpqrstvwxyzBCDEFGHJKLMNPQRSTVWXYZ' :
            b.upper()
                    
        i=i+1
        
        b= b + 1
        
    return b