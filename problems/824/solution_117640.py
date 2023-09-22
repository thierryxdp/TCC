def uppCons(frase):
    """função  recebe uma frase e retorna as 
    consoantes em letras maiusculas
    ent-str
    saida-str
    
    """
    n=''
    t=0
    while t<len(frase):
        con=frase[t]
        if con in 'bcdfghjklmnpqrstvwxyzç':
            con=str.upper(con)
        n+=con
        t+=1
    return n