def filtra_pares(x):
    """Filtra apenas os numeros pares da tupla x
    tupla-> tupla
    testes (1,2,3,4) = (2,4)
    (1,3,5,7)= ()"""           
    for n in range(len(x)):
        if n%2==0:
            return n