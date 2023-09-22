def soma_h(N):
    """Função que, dado um número inteiro N, calcula e retorna o valor H com N termos; int->float"""
    
    H = 0
    
    for x in range(1,(N+1)):

        H = H + 1/N

    return H