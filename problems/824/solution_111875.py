def uppCons(texto: str) -> str:
    """ Uma função que receba como entrada uma frase e retorne a frase com todas as suas consoantes em
maiúsculas e mantendo as demais do mesmo jeito"""
    
    i = 0
    
    while i < len(texto):
        frase = texto[i]
        
        if frase in "bcçdfghjklmnpqrstvxyz":
            nova_frase = str.upper(frase)
            texto = str.replace(texto,frase,nova_frase)
        	
        i = i + 1
        
    return texto