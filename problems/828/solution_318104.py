# Questão 5
def primo (numero):
    '''Função que dado um numero inteiro e positivo e primo nos retornará um valor booleano'''

    i = 1
    soma = 0
    while  i <= numero:
        if numero % i == 0:
            soma += 1
        i = i+1
    if soma == 2:
        return True
    else:
        return False