#Start your python function herei = 0
def filtra_pares(A):
    retorno=[]
    if (A[0]%2==0):
        retorno = A[0]
    if (A[1]%2)==0:
        retorno = retorno + A[1]       
    if (A[2]%2)==0:
        retorno = retorno + A[2]
    if (A[3]%2)==0:
        retorno = retorno + A[3]    
    return retorno