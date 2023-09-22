def filtra_pares(tupla):
    """Função que dada uma tupla com elementos separa os caracteres do tipo string dos demais e os organiza em uma nova tupla"""
    string= %2
    a,b,c,d=tupla
    if type(a) == str and type(b) == str and type(c) ==str and type(d)==str: 
        return (a, b, c, d), () 
    if type(a) == str and type(b) == str: 
        return (a, b), (c, d) 
    if type(a) == str and type(c) == str: 
        return (a, c), (b,d) 
    if type(b) == str and type(c)==str and type(d)==str: 
        return (b, c, d), (a,) 
    if type(c) == str: 
        return (c,), (a, b, d) 
    if type(a) == str: 
        return (a,), (b, c, d) 
    if type(b) == str: 
        return (b,), (a, c, d) 
    else: 
        return (), (a, b, c,d)