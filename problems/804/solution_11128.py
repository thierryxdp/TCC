#Start your python function here
def filtra_pares(int1,int2,int3,int4):
    """Função que retorna apenas numeros pares dentre os numeros inteiros de entrada
    entrada: int
    saida: int"""
    if not(int1 % 2 == 0 and int2 % 2 == 0 and int3 % 2 == 0):
        return (int4,)
    elif not(int1 % 2 == 0 and int2 % 2 == 0 and int4 % 2 == 0):
        return (int3,)
    if not(int1 % 2 == 0 and int3 % 2 == 0 and int4 % 2 == 0):
        return (int2,)
    elif not(int2 % 2 == 0 and int3 % 2 == 0 and int4 % 2 == 0):
        return (int1,)
    if not(int1 % 2 == 0 and int2 % 2 == 0):
        return (int3, int4)
    elif not(int1 % 2 == 0 and int3 % 2 == 0):
        return (int2, int4)
    if not(int1 % 2 ==0 and int4 % 2 == 0):
        return (int2, int3)
    elif not(int2 % 2 == 0 and int3 % 2 == 0):
        return (int1, int4)
    if not(int2 % 2 == 0 and int4 % 2 == 0):
        return (int1, int3)
    elif not (int3 % 2 == 0 and int4 % 2 == 0):
        return (int1, int2)
    if not int1 % 2 == 0:
        return (int2, int3, int4)
    elif not int2 % 2 ==0:
        return (int1, int3, int4)
    if not int3 % 2 ==0:
        return (int1, int2, int4)
    elif not int4 % 2 == 0:
        return (int1, int2, int3)
    else:
        return (int1, int2, int3, int4)