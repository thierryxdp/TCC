def soma_h(n):
    """Retorna o valor H com N termos onde N é inteiro e dado com entrada.
    int-->float"""
    soma=0
    for numero in list(range(1,n+1)):
        soma=soma+1/numero
    return round(soma,2)