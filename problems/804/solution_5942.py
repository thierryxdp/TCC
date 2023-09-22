def filtra_pares(a,b,c,d):
    a_par=int(a)%2 == 0
    b_par=int(b)%2 == 0
    c_par=int(c)%2 == 0
    d_par=int(d)%2 == 0
    if a_par and b_par and c_par and d_par:
        return (a,b,c,d)
    elif not(a_par) and b_par and c_par and d_par:
        return (b,c,d)
    elif a_par and not(b_par) and c_par and d_par:
        return (a,c,d)
    elif a_par and b_par and not(c_par) and d_par:
        return (a,b,d)
    elif a_par and b_par and c_par and not(d_par):
        return(a,b,c)
    else:
        return()