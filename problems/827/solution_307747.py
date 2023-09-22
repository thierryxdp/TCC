def qtd_divisores(n):
    """Dado um número n, a função calcula quantos divisores
    esse número tem e o retorna.
    Parametros de Entrada: int
    Retorna: int"""

    contador=0
    
    for i in list(range(1,n+1)):
        if (n%i)==0:
          contador=contador+1
    return contador