def fatorial(numero):
    """dado um número inteiro, a função retorna o fatorial desse número.
    int-->int
    
    Parâmetros
    numero: numero inteiro que terá seu fatorial calculado"""
    fator=numero-1
    while fator>1:
        numero=fator*numero
        fator=fator-1
    return numero