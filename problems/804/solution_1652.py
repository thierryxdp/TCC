def filtra_pares(n1,n2,n3,n4):
    par_n1 = False
    par_n2 = False
    par_n3 = False
    par_n4 = False
    if(type(n1 == str(n1))):
        int1 = int(n1)

    if(type(n2 == str(n2))):
        int2 = int(n2)

    if(type(n3 == str(n3))):
        int3 = int(n3)

    if(type(n4 == str(n4))):
        int4 = int(n4)

    if(int1%2 == 0):
        par_n1 = True
    if(int2%2 == 0):
        par_n2 = True
    if(int3%2 == 0):
        par_n3 = True
    if(int4%2 == 0):
        par_n4 = True

    if(par_n1 == True and par_n2 == True and par_n3 == True and par_n4 == True):
        return int1,int2,int3,int4