def lingua_p(palavra) :
    """Dada uma palavra em português, retorna sua tradução 
    na língua do P;
    str -> str"""
    novo = []
    x = 0
    P = palavra
    z = 0
    y = x 
    while x < len(palavra) : 
        y = x + 2*z
        if palavra[x] in 'AEIOUaeiou' :
            P = P[0:y+1] + "p" + P[y] + P[y+1:]
            z = z + 1 
            y = x + 2*z
            
        
        x = x + 1 
        
    
    
    return str.lower(P)