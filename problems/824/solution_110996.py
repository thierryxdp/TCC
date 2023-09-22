def uppCons(F):
    """Funcao que recebe como entrada uma frase F e retorna
    a frase com todas as suas consoantes em maiusculas(e os 
    demais caracteres exatamente como estavam na frase 
    original);
    str->str"""
    
    i=0
    maiuscula=''
    
    while i<len(F):
        if F[i] in "bcdfghjklmnpqrstvxwyzç":
        	maiuscula=str.upper(F[i])
        	F=str.replace(F,F[i],maiuscula)
        i=i+1
    return F