def uppCons(frase):
    """Retorna uma frase com todas as consoantes em maiúsculas;
    str -> str"""
    a = 0 
    y = frase
    while a < len(frase) : 
        if frase[a] in "zxcvbnmlçkjhgfdsqwrtypZXCVBNMÇLKJHGFDSQWRTYP":
            x = frase[a]
            y = str.replace(frase,x,str.upper(frase[a]),a)
        a = a + 1
    
    return  y