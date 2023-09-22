def soma_h(N):
    """Cálculo de uma função que calcula e retorna o valor de H com N termos.
      
       Parameters:
       N: termos inteiro
       
       Returns:
       Retorna o valor de H, dado que:
       int -> float."""
    soma=0
    for s in range(1,N+1):
        if 1/N!=0:
            soma=soma+1/N
    return round(soma,2)