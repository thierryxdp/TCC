def uppCons(frase):
    '''funcao que retorna todas as consoantes de uma frase
    maiúscula; str -> str'''
    
    b= frase
    i = 0
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    
    while i < len(frase):
        
        if consoantes in frase[i]:
            a = b.upper(consoantes)
            b.replace(consoantes,a, regex=True)
                    
        i=i+1
        
    return b