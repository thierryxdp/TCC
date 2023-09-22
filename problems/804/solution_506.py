def filtra_pares(int1, int2, int3, int4):
    """funcao que retorna uma tupla contendo apenas os elementos pares
       dentre os elementos inseridos na mesma ordem em que estavam
       
       int,int,int,int-> tupla
    """
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