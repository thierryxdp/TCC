def filtra_pares(T):
    """ recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla contendo apenas os elementos pares da tupla original
    entrada:tuple
    retorna:tuple"""
    a,b,c,d=T
    par_a= (a%2)==0
    par_b= (b%2)==0
    par_c= (c%2)==0
    par_d= (d%2)==0
    
    if par_a and par_b and par_c and par_d:
        return(a,b,c,d)
    elif par_a and par_b and par_c:
        return(a,b,c)
    elif par_a and par_b and par_d:
        return (a,b,d)
    elif par_a and par_c and par_d:
        return (a,c,d)
    elif par_b and par_c and par_d:
        return (b,c,d)
    elif par_a and par_b:
        return (a,b)
    elif par_a and par_c:
        return (a,c)
    elif par_a and par_d:
        return (a,d)
    elif par_b and par_c:
        return (b,c)
    elif par_b and par_d:
        return(b,d)
    elif par_c and par_d:
        return (c,d)
    elif par_a:
        return (a)
    elif par_b:
        return(b)
    elif par_c:
        return(c)
    elif par_d:
        return(d)
    else:
        return ('')