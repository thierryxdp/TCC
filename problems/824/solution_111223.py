def uppCons(frase):
    """Retorna a frase com todas as suas consoantes em maísculas.
    string --> string"""
    
    frase_maiscula = str.upper(frase)
    i = 0
    
    while i < len(frase_maiscula):
        if 'A' or 'E' or 'I' or 'O' or 'U' == frase_maiscula[i]:
         
            str.replace(frase_maiscula, frase_maiscula[i], str.lower(frase_maiscula[i]), 1)
        else:
            str.replace(frase_maiscula, frase_maiscula[i], frase_maiscula[i], 1)
            
        i = i + 1
        
    return frase_maiscula