# Questão 4 - MT
def soma_h(n):
    '''Calcula o valor da soma
    H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
    int --> float'''

    # variável para guardar o valor da soma
    soma = 0

    # itera pelo intervalo de 1 até n
    for i in range(1, n+1):
        # incrementa o próximo termo de H à variável soma
        soma += 1/i
    return round(soma)[0]