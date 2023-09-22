def uppCons(frase):
    """Retorna uma frase com todas as consoantes em maiúsculas;
    str -> str"""
    a = 0 
    y = frase
    while a < len(frase) : 
        if frase[a] in "zZxxcCvVbBnNmMçÇlLkKjJhHgGfFdDqQwWrRtTyYpP":
            x = frase[a]
            z = str.upper(frase[a])
            y = str.replace(frase,x,z,a)
        a = a + 1
    
    return  y