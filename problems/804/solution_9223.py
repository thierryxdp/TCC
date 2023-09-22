#Start your python function here
def filtra_pares(x):
    """
    n1,n2,n3,n4 estao dentro da tupl
    funcao retorna os numeros pares cintidos na mesma
    """"
    n1=x[0]
    n2=x[1]
    n3=x[2]
    n4=x[3]
    if (n1,n2,n3,n4)%2==0:
        return x