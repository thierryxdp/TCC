def filtra_pares(a):
    tupla_par = ()
    
    A1= a[1]
    A2= a[2]
    A3= a[3]
    A4= a[4]
    
    if(A1%2==0):
        return tupla_par = tupla_par + (A1,)
    if (A2%2==0):
        return tupla_par = tupla_par + (A2,)
    if(A3%3==0):
        return tupla_par = tupla_par + (A3,)
    if(A4%3==0):
        return tupla_par = tupla_par + (A4,)