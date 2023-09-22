def uppCons(frase):
    "função que transforma todas as consoantes da frase em maiúsculas"
    "str -> str'''
    i = 0
    frase_vazia = ''
    
    while i<len(frase):
        
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç': 
            frase_vazia = frase_vazia + frase[i].upper()
        else:
            frase_vazia = frase_vazia + frase[i]

        
        i = i + 1    
        
    return fraseNoba