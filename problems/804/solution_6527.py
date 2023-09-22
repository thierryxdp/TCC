def filtra_pares(tupla,i1,i2,i3,i4):
    '''recebe uma tuple com 4 inteiros como parâmetros e retorna uma nova
    tuple com os elementos pares da tupla; tuple,int,int,int,int -> tuple'''
    tupla = (i1,i2,i3,i4)
    NovaTupla = (0,0,0,0)
    s = i1%2
    t = i2%2
    p = i3%2
    a = i4%2
    if s == 0:
        NovaTupla[1] += (i1)
    elif t == 0:
        NovaTupla[2] += (i2)
    elif p == 0:
        NovaTupla[3] +=  (i3)
    elif a == 0:
        NovaTupla[4] += (i4)        
    return NovaTupla(i1,i2,i3,i4)