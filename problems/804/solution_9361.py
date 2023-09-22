def filtra_pares (int1,int2,int3,int4):
    """funcao que retorna tupla que contem somente os elementos pares de uma tupla dada;
       tuple->tuple""""
    pares= ()
    if (int1%2==0):
        pares= pares+ (int1,)
    elif (int2%2==0):
        pares= pares + (int2,)
    elif (int3%2==0):
        pares= pares + (int3,)
    elif (int4%2==0):
        pares= pares + (int4,)
    return pares