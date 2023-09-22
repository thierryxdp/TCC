def isVogal(c):
    if c in 'aeiouAEIOU':
        return True
    else:
        return False
        
def uppCons(frase):
    fraseReturn = ''
    
    cont = 0
    
    while(cont < len(frase)):
        if isVogal(frase[cont]) == False:
            fraseReturn += frase[cont].upper()
        else:
            fraseReturn += frase[cont]
        cont = cont + 1
        
    return fraseReturn