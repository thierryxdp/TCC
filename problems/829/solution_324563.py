def soma_h (N):
    """Função que dado n termos, retorne o resultado de sua soma com somente com 2 casas decimais.
    int -> float"""
    soma = 0
    for x in range(1,N+1):
        soma = soma + 1/x
    return round(soma,2)