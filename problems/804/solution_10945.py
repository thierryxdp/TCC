def filtra_pares(t):
    """dada uma tupla t, retorna uma nova tupla com os elementos pares de t na ordem em que aparecem"""
    """ tuple -> tuple"""
    tuplavazia = ()
    if (t[0]%2)==0:
        tuplavazia = tuplavazia + (t[0],)
    if (t[1]%2)==0:
        tuplavazia = tuplavazia + (t[1],)
    if (t[2]%2)==0:
        tuplavazia = tuplavazia + (t[2],)
    if (t[3]%2)==0:
        tuplavazia = tuplavazia + (t[3],)
        
    return tuplavazia