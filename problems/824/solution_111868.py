def uppCons(texto: str) -> str:
    
    i = 0
    
    while i < len(texto):
        frase = texto[i]
        
        if frase in "bcdfghjklmnpqrstvxyz":
            nova_frase = str.upper(frase)
            texto = str.replace(texto,frase,nova_frase)
        
        	
        i = i + 1
        
    return texto