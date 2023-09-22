def uppCons(frase):
    '''funcao que retorna todas as consoantes de uma frase
    maiúscula; str -> str'''
    
    b= frase
    i = 0
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDEFGHJKLMNPQRSTVWXYZ'
    
    while i < len(frase):
        
        if consoantes in frase[i]:
            a = b.upper()
                    
        i=i+1
        
        x = b.replace(consoantes,str.a)
        
    return x