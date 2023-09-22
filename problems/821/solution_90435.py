from math import factorial
def soma_fatorial(n):
    '''Calcula a soma dos fatoriais de 1 até n
    int --> int'''
      soma = 0
           for i in range(n, 0, -1):
                 soma += factorial(i)
            return soma