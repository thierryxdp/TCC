def qtd_divisores(numero):
    '''
    Programa que lê um inteiro positivos n 
    e verifica e imprime seus divisores int--> int.
    '''
divisor = 1
soma = 0
for divisor in range(1, numero):
    if numero % divisor == 0:
        soma += divisor
   return soma