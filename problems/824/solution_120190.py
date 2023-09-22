def uppcons(frase):
    alfabeto = 1
    frase_final = frase[0].upper()
    
    while alfabeto < len(frase):
        if frase[alfabeto] in ('b','c','C','ç','d','f','j','k','l','m','n','p','q','r','s','t','v','w','y','z')
        
        	frase_final += frase[alfabeto].upper()
        else:
            frase_final += frase[alfabeto].lower()
        alfabetp +=1
        
    return frase_final