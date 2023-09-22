def filtra_pares(a,b,c,d):
    ''' Recebe como entrada 4 números inteiros e filtra os pares, retornando-os;
    exemplo: '(1,2,3,4)'=>'(2,4)';
    int,int,int,int => tupla'''
    if int(a)%2==0 and int(b)%2==0 and int(c)%2==0 and int(d)%2==0:
        return (a,b,c,d)
    elif int(a)%2==0 and int(b)%2==0 and int(c)%2==0 and not int(d)%2==0:
        return(a,b,c)
    elif int(a)%2==0 and int(b)%2==0 and not int(c)%2==0 and int(d)%2==0:
        return(a,b,d)
    elif int(a)%2==0 and not int(b)%2==0 and int(c)%2==0 and int(d)%2==0:
        return(a,c,d)
    elif int(b)%2==0 and not int(a)%2==0 and int(c)%2==0 and int(d)%2==0:
        return (b,c,d)
    elif int(a)%2==0 and int(b)%2==0 and not int(c)%2==0 and not int(d)%2==0:
        return (a,b)
    elif int(a)%2==0 and not int(b)%2==0 and int(c)%2==0 and not int(d)%2==0:
        return(a,c)
    elif int(b)%2==0 and not int(a)%2==0 and int(c)%2==0 and not int(d)%2==0:
        return(b,c)
    elif int(a)%2==0 and not int(b)%2==0 and not int(c)%2==0 and int(d)%2==0:
        return (a,d)
    elif int(b)%2==0 and not int(a)%2==0 and not int(c)%2==0 and int(d)%2==0:
        return(b,d)
    elif int(c)%2==0 and not int(b)%2==0 and not int(a)%2==0 and int(d)%2==0:
        return(c,d)
    elif int(a)%2==0 and not int(b)%2==0 and not int(c)%2==0 and not int(d)%2==0:
        return(a)
    elif int(b)%2==0 and not int(a)%2==0 and not int(c)%2==0 and not int(d)%2==0:
        return(b)
    elif int(c)%2==0 and not int(b)%2==0 and not int(a)%2==0 and not int(d)%2==0:
        return(c)
    elif int(d)%2==0 and not int(b)%2==0 and not int(c)%2==0 and not int(a)%2==0:
        return(d)
    else:
        return ()