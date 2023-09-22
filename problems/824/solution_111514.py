def uppCons(frase):
    """Dada uma frase coloca suas consoantes em caixa alta. str -> str """
    
    i = 0
    nova_frase = ''
    while i < len(frase):
        
        
        if frase[i] in 'bcçdfghjklmnpqrstvxwyzBCÇDFGHJKLMNPQRSTVXWYZ':
            
            
            nova_frase = nova_frase + frase[i].upper()
        else:
            
            nova_frase = nova_frase + frase[i]
            
        i = i+1
        
    return nova_frase