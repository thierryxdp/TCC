from math import factorial
def soma_fatorial(n):
    '''Calcula a soma dos fatoriais de 1 até n
    int --> int'''

    # variável para guardar o valor da soma
    soma = 0

    # itera no intervalo de n até 1 com passo -1
    for i in range(n, 0, -1):
        # incrementamos a soma com o fatorial seguinte
        soma += factorial(i)
    return soma