def uppCons(frase) :
    """Dado uma frase, retorna a mesma frase, porém com todas
    as consoantes em maiúsculas;
    str -> str"""
    x = 0 
    f = frase
    while x < len(frase) :
        if frase[0] in 'czxvbnmçlkjhgfdsqwrtyp':
            a = str.upper(frase[0])
            f = a+frase[1:]
        elif frase[x+1] in 'czxvbnmçlkjhgfdsqwrtyp' :
            z = frase[x]
            y = str.upper(frase[x])
            f = str.replace(f,z,y,x)
            
        x = x + 1
        
    
    return f