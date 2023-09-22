def qtd_divisores(n):
    '''
    Programa que lê um inteiro positivos n 
    e verifica e imprime seus divisores int--> int.
    '''
    soma = 0
    for divisor in range(1,n):
        if n % divisor == 0:
            soma += divisor
            return soma