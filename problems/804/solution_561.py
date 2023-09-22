def filtra_pares(tupla):
    '''Função que recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla
contendo apenas os elementos pares da tupla original, na mesma ordem que se encontravam
    tupla(int,int,int,int) -> tupla
    '''
    if tupla[0]//2==tupla[0]/2:
        a = tupla[0]
    else:
        a = False
        
    if tupla[1]//2==tupla[1]/2:
        b = tupla[1]
    else:
        b = False
        
    if tupla[2]//2==tupla[2]/2:
        c = tupla[2]
    else:
        c = False
        
    if tupla[3]//2==tupla[3]/2:
        d = tupla[3]
    else:
        d = False
        
    if type(a)==int and type(b)==int and type(c)==int and type(d)==int:
        resultado = (a,b,c,d)
    elif type(a)!=int and type(b)==int and type(c)==int and type(d)==int:
        resultado = (b,c,d)
    elif type(a)==int and type(b)!=int and type(c)==int and type(d)==int:
        resultado = (a,c,d)
    elif type(a)==int and type(b)==int and type(c)!=int and type(d)==int:
        resultado = (a,b,d)
    elif type(a)==int and type(b)==int and type(c)==int and type(d)!=int:
        resultado = (a,b,c)
    elif type(a)==int and type(b)==int and type(c)!=int and type(d)!=int:
        resultado = (a,b)
    elif type(a)==int and type(b)!=int and type(c)==int and type(d)!=int:
        resultado = (a,c)
    elif type(a)==int and type(b)!=int and type(c)!=int and type(d)==int:
        resultado = (a,d)
    elif type(a)!=int and type(b)==int and type(c)==int and type(d)!=int:
        resultado = (b,c)
    elif type(a)!=int and type(b)==int and type(c)!=int and type(d)==int:
        resultado = (b,d)
    elif type(a)!=int and type(b)!=int and type(c)==int and type(d)==int:
        resultado = (c,d)
    elif type(a)==int and type(b)!=int and type(c)!=int and type(d)!=int:
        resultado = (a,)
    elif type(a)!=int and type(b)==int and type(c)!=int and type(d)!=int:
        resultado = (b,)
    elif type(a)!=int and type(b)!=int and type(c)==int and type(d)!=int:
        resultado = (c,)
    elif type(a)!=int and type(b)!=int and type(c)!=int and type(d)==int:
        resultado = (d,)
    else:
        resultado = ()
    
    return resultado