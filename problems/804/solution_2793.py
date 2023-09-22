#Start your python function here
def filtra_pares(A):
    '''Função que recebe uma tupla e retorna uma tupla com os valores pares
tupla->tupla'''
    retorno=()
    if (A[0]%2==0):
        a= A[0]
    if (A[1]%2)==0:
        b = a , A[1]
    if (A[2]%2)==0:
        c= b , A[2]
    if (A[3]%2)==0:
        d = c , A[3]    
    return a,b,c,d