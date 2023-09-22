def uppCons(frase):
    """Retorna uma frase com todas as consoantes em maiúsculas;
    str -> str"""
    a = 0 
    while a < len(frase) : 
        if frase[a] in "zxcvbnmlçkjhgfdsqwrtypZXCVBNMÇLKJHGFDSQWRTYP":
            y = frase[a]
            z = str.upper(frase[a])
            str.replace(frase,y,z,a)
        a = a + 1
    
    return frase