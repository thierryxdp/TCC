def filtra_pares(tupla):
    '''função que recebe uma tupla com 4 números inteiros e retorna uma tupla que
       contém só os elementos pares desta tupla. tuple(int,int,int,int) -> tuple'''
    t1 = tupla
    t2 = ()
    t3 = ()
    t4 = ()
    t5 = ()
    if (t1[0] % 2 == 0):
        t2 = t2 + (t1[0],)
    else:
        t2 = ()
    if (t1[1] % 2 == 0):
        t3 = t3 + (t1[1],)
    else:
        t3 = ()
    if (t1[2] % 2 == 0):
        t4 =  t4 + (t1[2],)
    else:
        t4 = ()
    if (t1[3] % 2 == 0):
        t5 = t5 + (t1[3],)
    else:
        t5 = ()
        return t2 + t3 + t4 + t5