def soma_h(numero):
    """Retorne o valor com N termos, onde N é inteiro e é o numero de entrada, retorne seu valor somente com 2 casas decimais"""
    soma = 0
    for i in range(1, numero +1):
        divi = 1/i
        soma = divi
    return round(soma,2)