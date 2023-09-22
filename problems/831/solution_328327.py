def lingua_p(palavra) :
    """Dada uma palavra em português, retorna sua tradução 
    na língua do P;
    str -> str"""
    novo = []
    x = 0
    while x < len(palavra) : 
        if palavra[x] in 'AEIOUaeiou' :
            list.append(novo,x)
        
        x = x + 1  
        
    for y in novo :
        P = palavra[0:y+1] + "p" + palavra[y] + palavra[y+1:]
        y = y + 2 
        
    return str.lower(P)