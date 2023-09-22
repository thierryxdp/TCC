#Start your python function here
def filtra_pares(valores):
    n1,n2,n3,n4 = valores
   
    if (n1 % 2 == 0) and (n2 % 2 != 0 and n3 % 2 != 0 and n4 % 2 != 0):
        return (n1)
    if (n2 % 2 == 0) and (n1 % 2 != 0 and n3 % 2 != 0 and n4 % 2 != 0):
        return (n2)
    if (n3 % 2 == 0) and (n1 % 2 != 0 and n2 % 2 != 0 and n4 % 2 != 0):
        return (n3)
    if (n4 % 2 == 0) and (n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0):
        return (n4,)
    elif (n1 % 2 == 0 and n2 % 2 == 0) and (n3 % 2 != 0 and n4 % 2 != 0):
        return (n1,n2)
    elif (n1 % 2 == 0 and n3 % 2 == 0) and (n2 % 2 != 0 and n4 % 2 != 0):
        return (n1,n3)
    elif (n1 % 2 == 0 and n4 % 2 == 0) and (n2 % 2 != 0 and n3 % 2 != 0):
        return (n1,n4)
    elif (n2 % 2 == 0 and n3 % 2== 0) and (n1 % 2 != 0 and n4 % 2 != 0):
        return (n2,n3)
    elif (n2 % 2 == 0 and n4 % 2 == 0) and (n3 % 2 != 0 and n1 % 2 != 0):
        return (n2,n4)
    elif (n3 % 2 == 0 and n4 % 2 == 0) and (n2 %2 != 0  and n1 % 2 != 0):
        return (n3,n4)
    elif (n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0) and (n4 % 2 != 0):
        return (n1,n2,n3)
    elif (n1 % 2 == 0 and n3 % 2 == 0 and n4 % 2 == 0) and (n2 % 2 != 0):
        return (n1,n3,n4)
    elif (n2 % 2 == 0 and n3 % 2 == 0 and n4 % 2 == 0) and (n1 % 2 != 0):
        return (n2,n3,n4)
    elif n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0 and n4 % 2 != 0:
        return ()
    else :
        return (n1,n2,n3,n4)