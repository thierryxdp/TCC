def filtra_pares(tupla):
    '''dada uma tupla com quatro numeros inteiros, retorna uma tupla com apenas os
    elementos pares da tupla original, na mesma ordem que se encontravam;
    tupla(int, int, int, int) --> tupla(int)'''
    a, b, c, d = tupla

    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)
    elif a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        return (b,c,d)
    elif a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        return (a,c,d)
    elif a%2==0 and b%2==0 and c%2!=0 and d%2==0:
        return (a,b,d)
    elif a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        return(a,b,c)
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        return (c,d)
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
        return (b,d)
    elif a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
        return (b,c)
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
        return (a,d)
    elif a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
        return (a,c)
    elif a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
        return (a,b)
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2!=0:
        return(a,)
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2!=0:
        return(b,)
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2!=0:
        return(c,)
    elif a%2!=0 and b%2!=0 and c%2!=0 and d%2==0:
        return(d,)
    else:
        return()