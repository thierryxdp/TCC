def filtra_pares (tupla):
    """funcao que retorna tupla que contem somente os elementos pares de uma tupla dada;
       tuple->tuple"""
    (int1,int2,int3,int4)= tupla
    pares= ()
    if int1%2==0:
        pares= pares+(int1,)
    if int2%2==0:
       pares= pares+(int2,)
    if int3%2==0:
        pares= pares+(int3,)
    if int4%2==0:
        pares= pares+(int4,)
    return pares