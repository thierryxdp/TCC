#Start your python function here
def filtra_pares(int1,int2,int3,int4):
    """Função que retorna apenas numeros pares dentre os numeros inteiros de entrada
    entrada: int
    saida: int"""
    if int1 % 2 != 0 and int2 % 2 != 0 and int3 % 2 != 0:
        return int4,
    elif int1 % 2 != 0 and int2 % 2 != 0 and int4 % 2 != 0:
        return int3,
    if int1 % 2 != 0 and int3 % 2 != 0 and int4 % 2 != 0:
        return int2,
    elif int2 % 2 != 0 and int3 % 2 != 0 and int4 % 2 != 0:
        return int1,
    if int1 % 2 != 0 and int2 % 2 != 0:
        return int3, int4
    elif int1 % 2 != 0 and int3 % 2 != 0:
        return int2, int4
    if int1 % 2 !=0 and int4 % 2 != 0:
        return int2, int3
    elif int2 % 2 != 0 and int3 % 2 != 0:
        return int1, int4
    if int2 % 2 != 0 and int4 % 2 != 0:
        return int1, int3
    elif int3 % 2 != 0 and int4 % 2 != 0:
        return int1, int2
    if int1 % 2 != 0:
        return int2, int3, int4
    elif int2 % 2 !=0:
        return int1, int3, int4
    if int3 % 2 !=0:
        return int1, int2, int4
    elif int4 % 2 !=0:
        return int1, int2, int3
    else:
        return int1, int2, int3, int4