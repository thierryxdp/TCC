def fatorial(N):
    """Dado um número inteiro positivo como entrada, a função calcula o fatorial
    deste número;
    int->int"""
    resultado=1
    i=1
    while i <= N:
        resultado=resultado*i
        i=i+1
    return resultado