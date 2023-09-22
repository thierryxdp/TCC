def uppCons(frase):
    '''teste'''
    novafrase=''
    i=0
    consoantes= 'bcdfghjklmnpqrstvwxyz'
    
    while i < len(frase):
        if frase[i] in consoantes:
            novafrase=novafrase+ str.upper(frase[i])
           
        
        i=i+1
        
    return novafrase