#Start your python function here
#tuple->tuple
def filtra_pares(t):
    """Função que retorna uma tupla contendo somente os elementos pares dentre
    os quatro da tupla inserida, na ordem em que são apresentados"""
    a=t[0]
    b=t[1]
    c=t[2]
    d=t[3]
    r=()
    if a%2==0:
        r=(a,)
    if b%2==0:
        r=r+(b,)
    if c%2==0:
        r=r+(c,)
    if d%2==0:
        r=r+(d,)
    return r