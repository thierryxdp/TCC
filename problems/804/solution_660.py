#Start your python function herei = 0
def filtra_pares(A):
    i=0
    retorno=[]
    if (A[0]%2==0):
        retorno[i] = A[0]
        i = i + 1
    if (A[1]%2)==0:
        retorno[i] = A[1]
        i = i + 1        
    if (A[2]%2)==0:
        retorno[i]=A[2]
        i = i + 1
    if (A[3]%2)==0:
        retorno[i]=A[3]    
    return retorno