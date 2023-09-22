def filtra_pares (A,B,C,D):
    if A%2==0:
        F=A
    else:
        F=()
    if B%2==0:
        I=B
    else:
        I=()
    if C%2==0:
        L=C
    else:
        L=()
    if D%2==0:
        T=D
    else:
        T=()
        
    return (F,I,L,T)