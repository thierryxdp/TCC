#Start your python function here
def filtra_pares(x):
    """
    n1,n2,n3,n4 estao dentro da tupl
    funcao retorna os numeros pares contidos na mesma
    """"
    x2= ()
    if x[0]%2==0:
        x2+=(x[0],)
    if x[1]%2==0:
        x2+=(x[1],)
    if x[2]%2==0:
        x2+=(x[2],)
    if x[3]%2==0:
        x2+=(x[3],)
    return x2