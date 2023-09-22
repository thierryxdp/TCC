def uppCons(frase):
    """Dada uma frase retorna esta com suas consoantes em maiúsculo.
       str -> str"""
    
    nova = ''
    i = 0
    
    while i < len(frase):
        if frase[i] in 'qwrtypçlkjhgfdszxcvbnm':
            nova = nova + frase[i].upper()
        else:
            nova = nova + frase[i]
        i += 1
        
    return nova