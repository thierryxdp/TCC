def uppCons(frase) :
    """Dado uma frase, retorna a mesma frase, porém com todas
    as consoantes em maiúsculas;
    str -> str"""
    x = 0 
    f = frase
    while x < len(frase) :
        if frase[x] in 'zxcvbnmçlkjhgfdsqwrtyp' :
            z = frase[x]
            y = str.upper(frase[x])
            f = str.replace(f,z,y,x)
            
        x = x + 1
    
    return f