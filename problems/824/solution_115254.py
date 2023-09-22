def uppCons(frase):
    '''funcao que retorna todas as consoantes de uma frase
    maiúscula; str -> str'''
    
    b= frase
    i = 0
    consoantes = ('bcdfghjklmnpqrstvwxyz')
    while i < len(frase):
        
        if frase in consoantes:
           	b = consoantes.upper()
                                
        i=i+1
        
    return b