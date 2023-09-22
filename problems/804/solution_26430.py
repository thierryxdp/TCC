#int -> tuple
def filtra_pares(num):
    #defino o novo conjunto com os pares
    pares=()
    #avalio cada elemento da tupla num
    if num[0]%2==0:
        pares+=(num[0],)
    if num[1]%2==0:
        pares+=(num[1],)
    if num[2]%2==0:
        pares+=(num[2],)
    if num[3]%2==0:
        pares+=(num[3],)
    return pares