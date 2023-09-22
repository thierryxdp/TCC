def filtra_pares(A):
    a=A[0]%2==0        
    b=A[1]%2==0
    c=A[2]%2==0
    d=A[3]%2==0
    return a,b,c,d

def filtra_pares(A):
    '''Função que recebe uma tupla e retorna uma tupla com os valores pares
tupla->tupla'''
    retorno=()
    if (A[0]%2==0):
        a= A[0]
    if (A[1]%2)==0:
        b= A[1]
    if (A[2]%2)==0:
        c =A[2]
    if (A[3]%2)==0:
        d=A[3]
    else:
        return a,b,c,d