import math
def qtd_divisores(n):
     '''Função que conte quanto divisores um dado número inteiro tem.
       int ---> lista de inteiros'''
     divisores = [1]
     for i in range(2,int(math.sqrt(n)) + 1):
         if n % i == 0:
             divisores.extend([i, n // i])
             divisores.extend([n])
    return list((divisores))