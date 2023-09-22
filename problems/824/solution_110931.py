def uppCons(F1):
    """Funcao que recebe como entrada uma frase F1 e retorna
    a frase com todas as suas consoantes em maiusculas(e os 
    demais caracteres exatamente como estavam na frase 
    original);
    str->str"""
    
    i=0
    maiuscula=''
    F2=F1[:]
    
    while i<len(F2):
        if F2[i] in "bcdfghjklmnpqrstvxwyz":
        	maiuscula=str.upper(F2[i])
        	str.replace(F2,F2[i],maiuscula)
        i=i+1
    return F2