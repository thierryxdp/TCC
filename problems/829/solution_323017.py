def soma_h(N):
    """funcao que calcula e retorna o valor H com N termos.
    int -> float"""
    contagem = 0
    soma = 0
    while contagem < N:
        soma +=1/(contagem+1)
        contagem += 1
    return round(soma,2)