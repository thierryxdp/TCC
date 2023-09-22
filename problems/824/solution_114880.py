def uppCons(frase):
    '''funcao que retorna todas as consoantes de uma frase
    maiúscula; str -> str'''
    
    b= frase
    i = 0
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDEFGHJKLMNPQRSTVWXYZ'
    
    while i < len(frase):
        
        if consoantes in frase[i]:
            b.upper()
            x = b.replace(frase,consoantes,a)
                    
        i=i+1
        
    return x