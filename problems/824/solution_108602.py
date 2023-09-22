def uppCons (frase):
    """funçao que recebe uma frase e retorna a frase com todas as suas consoantes em maiusculas
    entrada: str;
    saida: str."""
    
    i = 0
    
    while i < len (frase):
        
        if 'bcdfghjklmnpqrstvxywz' in frase:
            
            frase = list (frase)
            upper = str.upper (frase [i])
            del (frase [i])
            list.insert (frase, i, upper)
        
        i = i + 1
        return frase