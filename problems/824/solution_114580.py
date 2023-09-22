def uppCons(frase):
    """retorna a frase com todas as suas consoantes em maiusculas;
    str -> str"""
    i=0
    m=''
    
    while i<len(frase):
        if frase[i]  not in 'aeiouAEIOU':
            m=m+str.upper(frase[i])
        else:
            m=m+frase[i]
        i=i+1
    return m