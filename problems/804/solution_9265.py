#Start your python function here
def filtra_pares(x):
    """
    n1,n2,n3,n4 estao dentro da tupl
    funcao retorna os numeros pares contidos na mesma
    """"
    n1=x[0]
    n2=x[1]
    n3=x[2]
    n4=x[3]
    resultado=()
    if n1%2==0:
        resultado=resultado+(n1,)
    if n2%2==0:
            resultado=resultado+(n2,)
    if n3%2=0:
            resultado=resultado+(n3,)
    if n4%2==0:
            resultado=resultado+(n4,)
            return resultado
    else:
            return x[]