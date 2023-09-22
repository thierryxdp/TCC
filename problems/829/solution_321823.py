def soma_h(N):
    """Função que dado um número inteiro 'N', calcula e retorna o valor de H com
    N termos; int -> float"""

    somaH = 0

    for dividendo in range(1,N+1):
        somaH += (1/dividendo)

    return round(somaH,2)