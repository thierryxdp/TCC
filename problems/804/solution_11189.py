#Start your python function here
def filtra_pares(int1,int2,int3,int4):
    """Função que retorna apenas numeros pares dentre os numeros inteiros de entrada
    entrada: int
    saida: int"""
    a = filtra_pares[1:]
    b = filtra_pares[0:1]
    c = filtra_pares[2:]
    d = filtra_pares[0:2]
    e = filtra_pares[3:]
    f = filtra_pares[0:3] 
    g = filtra_pares[1:3]
    h = filtra_pares[2:3]
    if int1 % 2 != 0:
        return a
    elif int2 % 2 != 0:
        return b + c
    if int3 % 2 != 0:
        return d + e
    elif int4 % 2 != 0:
        return f
    if int1 % 2 != 0 and int2 % 2 != 0:
        return c
    elif int3 % 2 != 0 and int4 % 2 != 0:
        return d
    if int1 % 2 != 0 and  int3 % 2 != 0:
        return d + e
    elif int1 % 2 != 0 and int4 % 2 != 0:
        return g
    if int2 % 2 != 0 and int3 % 2 != 0:
        return b + e
    elif int2 % 2 != 0 and int4 % 2 != 0:
        return b + h
    if int1 % 2 != 0 and int2 % 2 != 0 and int3 % 2 != 0:
        return e
    elif int1 % 2 != 0 and int2 % 2 != 0 and int4 % 2 != 0: