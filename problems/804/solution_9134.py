def filtra_pares(tupl):
    '''
    retorna os números pares da tupla inserida.
    tuple->tuple
    '''
    t0=()
    t1=()
    t2=()
    t3=()
    if tupl[0]%2==0:
        t0=(tupl[0],)
    if tupl[1]%2==0:
        t1=(tupl[1],)
    if tupl[2]%2==0:
        t2=(tupl[2],)
    if tupl[3]%2==0:
        t3=(tupl[3],)
    return (t0)+(t1)+(t2)+(t3)