def filtra_pares(tupla):
    """Função que dada uma tupla com elementos separa os caracteres do tipo string dos demais e os organiza em uma nova tupla"""
    a,b,c,d =tupla
    numero = int(input(' ')) 
    if type(a%2) == 0 or 1 and type(b%2) == 0 or 1 and type(c%2) ==0 or 1 and type(d%2)==0 or 1: 
        return (a, b, c, d), () 
    if type(a%2) == 0 or 1 or 1 and type(b%2) == 0 or 1: 
        return (a, b), (c, d) 
    if type(a%2) == 0 or 1 and type(c%2) == 0 or 1: 
        return (a, c), (b,d) 
    if type(b%2) == 0 or 1 and type(c%2)==0 or 1 and type(d%2)==0 or 1: 
        return (b, c, d), (a,) 
    if type(c%2) == 0 or 1: 
        return (c,), (a, b, d) 
    if type(a%2) == 0 or 1: 
        return (a,), (b, c, d) 
    if type(b%2) == 0 or 1: 
        return (b,), (a, c, d) 
    else: 
        return (), (a, b, c, d)