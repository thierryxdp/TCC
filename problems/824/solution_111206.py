def uppCons(frase):
    """Retorna uma frase com todas as consoantes em maiúsculas;
    str -> str"""
    a = 0 
    y = frase
    while a < len(frase) : 
        if frase[a] in "zxcvbnmlçkjhgfdsqwrtypZXCVBNMÇLKJHGFDSQWRTYP":
            y = str.replace(frase,frase[a],str.upper(frase[a]),a))
        a = a + 1
    
    return  y