def qtd_divisores(num):
    '''
    Programa que lê um inteiro positivos n 
    e verifica e imprime seus divisores int--> int.
    '''
for i in range(1, num//2+1):
      if num % i == 0: 
        yield i
yield num