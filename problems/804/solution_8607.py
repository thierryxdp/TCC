# Temos uma tupla com 4 elementos inteiros e queremos uma nova tupla com
# apenas seus elementos pares e na mesma ordem em que se encontravam.
# tuple -> tuple

def filtra_pares(int1, int2,  int3, int4):
    '''Dada uma tupla com 4 elementos inteiros, devolve uma nova tupla com
    apenas seus elementos pares e na mesma ordem em que se encontravam;
    tuple -> tuple'''
    if (int1 % 2) == 0:
        if (int2 % 2) == 0:
            if (int3 % 2) == 0:
                if (int4 % 2) == 0:
                    return (int1, int2,  int3, int4)
                else:
                    return (int1, int2,  int3)
            else:
                return (int1, int2)
        else:
            return (int1)
    else:
        return ()