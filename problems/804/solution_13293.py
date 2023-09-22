def filtra_pares(num):
    """Dado um conjunto de quatro números (a,b,c,d), filtra os números
    ímpares e retorna pares:
    truple-->truple"""
    n1=num[0]
    n2=num[1]
    n3=num[2]
    n4=num[3]
    c1=int(n1)%2!=0
    c2=int(n2)%2!=0
    c3=int(n3)%2!=0
    c4=int(n4)%2!=0
    if c1 and not(c2 or c3 or c4):
        return ('',n2,n3,n4)
    elif c2 and not(c1 or c3 or c4):
        return (n1,'',n3,n4)
    elif c3 and not(c1 or c2 or c4):
        return (n1,n2,'',n4)
    elif c4 and not(c1 or c2 or c3):
        return (n1,n2,n3,'')
    elif c1 and c2 and not(c3 or c4):
        return ('','',n3,n4)
    elif c1 and c3 and not(c2 or c4):
        return ('',n2,'',n4)
    elif c1 and c4 and not(c3 or c4):
        return ('',n2,n3,'')
    elif c2 and c3 and not(c1 or c4):
        return (n1,'','',n4)
    elif c2 and c4 and not(c1 or c3):
        return (n1,'',n3,'')
    elif c3 and c4 and not(c1 or c2):
        return (n1,n2,'','')
    elif c1 and c2 and c3 and not c4:
        return ('','','',n4)
    elif c2 and c3 and c4 and not c1:
        return (n1,'','','')
    elif c1 and c2 and c3 and c4:
        return ('','','','')
    else:
        return (n1,n2,n3,n4)