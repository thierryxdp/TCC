import math
def qtd_divisores(n):
     '''Função que conte quanto divisores um dado número inteiro tem.
       int ---> lista de inteiros'''
        divisores = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisores.append(i)
    return len(divisores)