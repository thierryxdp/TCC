def filtra_pares(a,b,c,d):
    A = a % 2
    B  = b % 2
    C = c % 2
    D = d % 2
    if not bool(A) and bool(B) and bool(C) and bool(D)==True:
        return (a,b,c,d)