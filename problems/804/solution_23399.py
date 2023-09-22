def filtra_pares(a,b,c,d):
    "função que recebe uma tupla com quatro elementos a,b,c,d e retorna uma nova tupla com os elementos pares da tupla anterior"
    if (a//2==0) and (b//2==0) and (c//2==0) and (d//2==0):
        return (a,b,c,d)
    elif 	(a and b and c)//2==0:
        return (a,b,c)
    elif	(d and b and c)//2==0:
        return (b,c,d)
    elif	(a and b and d)//2==0:
        return (a,b,d)
    elif	(a and d and c)//2==0:
        return (a,c,d)
    elif	(a and b)//2==0:
        return (a,b)
    elif	(a and c)//2==0:
        return (a,c)
    elif	(a and d)//2==0:
        return (a,d)
    elif	(b and c)//2==0:
        return (b,c)
    elif	(b and d)//2==0:
        return (b,d)
    elif	(c and d)//2==0:
        return (c,d)