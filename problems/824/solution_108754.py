def uppCons (frase):
    """funçao que recebe uma frase e retorna a frase com todas as suas consoantes em maiusculas
    entrada: str;
    saida: str."""
    
    pos = 0
    nova = ''
    
    while pos < len (frase):
        if frase [pos] in 'bcdfghjklmnpqrstvxyz':
            nova = nova + str.upper(frase [pos])
        else:
            nova = nova + frase [pos]
        
        pos = pos + 1
    
    return nova