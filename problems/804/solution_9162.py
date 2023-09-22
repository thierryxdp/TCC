#Start your python function here
def filtra_pares(n1,n2,n3,n4):
    par = ()
    if (n1%2==0):
         par = par + str(n1,)
    if (n2%2==0):
         par = par + str(n2,)
    if (n3%2==0):
         par = par + str(n3,)
    if (n4%2==0):
         par = par + str(n4,)
    if (n1%2==0) and (n2%2==0) and (n3%2==0) and (n4%2==0):
        par = par + str(n1,) + str(n2,) + str(n3,) + str(n4,)
    return par