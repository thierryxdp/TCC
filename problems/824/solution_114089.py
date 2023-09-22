#Questão2
def uppCons(frase):
    '''Função que transforma todas as consoantes da frase em maiúsculas
    string -> string'''
    i = 0
    fraseNoba = ''
    
    while i<len(frase):
        
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç': 
            fraseNoba = fraseNoba + frase[i].upper()
        else:
            fraseNoba = fraseNoba + frase[i]

        
        i = i + 1    
        
    return frase1