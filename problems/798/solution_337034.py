from math import factorial
def freq_palavras(frase):
    '''Calcula a soma dos fatoriais de 1 até n
    int --> int'''
    soma = 0
    for i in range(frase, 0, -1):
        soma += factorial(i)
    return soma