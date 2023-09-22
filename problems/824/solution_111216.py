def uppCons(frase):
    """Retorna a frase com todas as suas consoantes em maísculas.
    string --> string"""
    
    frase_maiscula = str.upper(frase)
    frase_final = []
    i = 0
    
    while i < len(frase_maiscula):
        if 'A' or 'E' or 'I' or 'O' or 'U' in frase_maiscula[i]:
            str.lower(frase_maiscula[i])
            list.append(frase_final, frase_maiscula[i])
        else:
            list.append(frase_final, frase_maiscula[i])
            
        i = i + 1
        
    return frase_final