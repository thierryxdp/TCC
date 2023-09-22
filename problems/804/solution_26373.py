def filtra_pares(A,B,C,D):
    pares=()
    inteiros=(A,B,C,D)
    if inteiros[A]%2==0:
        pares+=A
    if inteiros[1]%2==0:
        pares+=B
    if inteiros[2]%2==0:
        pares+=C
    if inteiros[3]%2==0:
        pares+=D
    return pares
#Start your python function here