def filtra_pares(t):
    ''' É uma função que filtra uma tuple,t, de quatro termos e devolve uma tuple com 
    apenas os elementos pares da tuple original. tuple-> tuple.'''
    n1=t[0]
    n2=t[1]
    n3=t[2]
    n4=t[3]
    if(n1%2==n2%2==n3%2==n4%2==0):
        return (n1,n2,n3,n4)
    elif(n1%2==n2%2==n3%2==0 and n4!=0):
        return(n1,n2,n3)
    elif(n1%2==n2%2==n4%2==0 and n3!=0):
        return(n1,n2,n4)
    elif(n1%2==n3%2==n4%2==0 and n2!=0):
        return(n1,n3,n4)
    elif(n2%2==n3%2==n4%2==0 and n1!=0):
        return(n2,n3,n4)
    
    elif(n1%2==n2%2==0 and n3%2!=0 and n4!=0):
        return(n1,n2)
    elif(n1%2==n3%2==0 and n2%2!=0 and n4!=0):
        return(n1,n3)
    elif(n1%2==n4%2==0 and n3%2!=0 and n2!=0):
        return(n1,n4)
    elif(n3%2==n2%2==0 and n1%2!=0 and n4!=0):
        return(n2,n3)
    elif(n4%2==n2%2==0 and n3%2!=0 and n1!=0):
        return(n2,n4)
    elif(n3%2==n4%2==0 and n1%2!=0 and n2!=0):
        return(n3,n4)
    
    elif(n1%2==0 and n2%2!=0 and n3%2!=0 and n4!=0):
        return(n1,)
    elif(n2%2==0 and n1%2!=0 and n3%2!=0 and n4!=0):
        return(n2,)
    elif(n3%2==0 and n2%2!=0 and n1%2!=0 and n4!=0):
        return(n3,)
    elif(n4%2==0 and n2%2!=0 and n3%2!=0 and n1!=0):
        return(n4,)
    
    
    elif(n1%2!=0 and n2%2!=0 and n3%2!=0 and n4!=0):
        return()