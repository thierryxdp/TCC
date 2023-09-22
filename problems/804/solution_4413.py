def filtra_pares(tupla):
    """Função que dada uma tupla com elementos separa os caracteres do tipo string dos demais e os organiza em uma nova tupla"""
    a,b,c,d =tupla
    if type(a%2) == 0 and type(b%2) == 0 and type(c%2) ==0 and type(d%2)==0: 
        return (a, b, c, d), () 
    if type(a%2) == 0 and type(b%2) == 0: 
        return (a, b), (c, d) 
    if type(a%2) == 0 and type(c%2) == 0: 
        return (a, c), (b,d) 
    if type(b%2) == 0 and type(c%2)==0 and type(d%2)==0: 
        return (b, c, d), (a,) 
    if type(c%2) == 0: 
        return (c,), (a, b, d) 
    if type(a%2) == 0: 
        return (a,), (b, c, d) 
    if type(b%2) == 0: 
        return (b,), (a, c, d) 
    else: 
        return (), (a, b, c,d)