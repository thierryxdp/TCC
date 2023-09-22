#Start your python function here
def filtra_pares(a,b,c,d):
    '''Esta função retorna uma nova tupla apenas com os valores
    pares da tupla dada
    int, int, int, int -> int'''
    if (a//2) == 0:
        if (b//2) == 0:
            if (c//2) == 0:
                if (d//2) == 0:
                    return (a,b,c,d)
                else:
                    return (a,b,c)
            else:
                return (a,b)
        else:
            return (a)