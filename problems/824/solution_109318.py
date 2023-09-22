def uppCons(frase):
    """Dada uma frase retorna esta com suas consoantes em maiúsculo.
       str -> str"""
    
    nova = ''
    contador = 0
    
    while contador < len(frase):
        if frase[contador] in 'qwrtypçlkjhgfdszxcvbnm':
            nova = nova + frase[contador].upper()
        else:
            nova = nova + frase[contador]
        contador += 1
        
    return nova