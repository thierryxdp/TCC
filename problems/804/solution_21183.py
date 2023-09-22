def filtra_pares(x):
    n1=x[0]
    n2=x[1]
    n3=x[2]
    n4=x[3]
    if n1%2==0:
        if n2%2==0:    
            if n3%2==0:
                if n4%2==0:
                    return (n1,n2,n3,n4)
                else:
                    return (n1,n2,n3)
            else:
                return (n1,n2)
        else:
            return 
     else:
        return '()'