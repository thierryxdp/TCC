def soma_h(n):
    """função que recebe um número inteiro n e calcula a 
    expressão H, onde os dividendos são os números que estão
    no intervalo de 1 até n
    int -> float"""
    intervalo = range(1,n+1)
    quocientes = []

    for numero in intervalo:
        quocientes += [1/numero]
    soma = sum(quocientes)

    return round(soma,2)