def soma_h(N):
    """funcao que retorna o valor de uma soma com n termos;
    int -> float"""

    H = 0

    for termo in range(1,N+1):

        H = H + 1/termo
        

    return rund(H,2)