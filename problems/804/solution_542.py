def filtra_pares(x):
    """funcao que retorna uma tupla contendo apenas os elementos pares
       dentre os elementos inseridos na mesma ordem em que estavam
       
       int,int,int,int-> tupla
    """

    int1 = x[0]
    int2 = x[2]
    int3 = x[3]
    int4 = x[4]

    if int1%2==0 and int2%2==0 and int3%2==0 and int4%2==0:
        return (int1, int2, int3, int4)
    elif int1%2!=0 and int2%2==0 and int3%2==0 and int4%2==0:
        return (int2, int3, int4)
    elif int1%2==0 and int2%2!=0 and int3%2==0 and int4%2==0:
        return (int1, int3, int4)
    elif int1%2==0 and int2%2==0 and int3%2!=0 and int4%2==0:
        return (int1, int2, int4)
    elif int1%2==0 and int2%2==0 and int3%2==0 and int4%2!=0:
        return (int1, int2, int3)
    elif int1%2!=0 and int2%2!=0 and int3%2==0 and int4%2==0:
        return t(int3, int4)
    elif int1%2!=0 and int2%2==0 and int3%2!=0 and int4%2==0:
        return (int2, int4)
    elif int1%2!=0 and int2%2==0 and int3%2==0 and int4%2!=0:
        return (int2, int3)
    elif int1%2==0 and int2%2!=0 and int3%2!=0 and int4%2==0:
        return (int1, int4)
    elif int1%2==0 and int2%2!=0 and int3%2==0 and int4%2!=0:
        return (int1, int3)
    elif int1%2==0 and int2%2==0 and int3%2!=0 and int4%2!=0:
        return (int1,int2)
    elif int1%2==0 and int2%2!=0 and int3%2!=0 and int4%2!=0:
        return (int1)
    elif int1%2!=0 and int2%2==0 and int3%2!=0 and int4%2!=0:
        return (int2)
    elif int1%2!=0 and int2%2!=0 and int3%2==0 and int4%2!=0:
        return (int3)
    elif int1%2!=0 and int2%2!=0 and int3%2!=0 and int4%2==0:
        return (int4)
    elif int1%2!=0 and int2%2!=0 and int3%2!=0 and int4%2!=0:
        return ()
#Start your python function here