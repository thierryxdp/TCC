def soma_h(N):
    """Recebe um número inteiro positivo N e retorna o valor o valor de H com N termos
       onde H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.
       int->float

       Parameters:
       N: O número de termos de H."""
    H=0
    for termo in range(1,N+1):
        H=H+1/termo
    return H