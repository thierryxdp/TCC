def soma_h(N):
    """Funcao que calcula e retorna o valor H = 1+(1/2)+(1/3)+...+(1/N), 
    sendo que N é um numero inteiro; int -> float"""

    H = 0

    for numero in range(1,N+1):
        H = H + 1/numero
    return round(H,2)