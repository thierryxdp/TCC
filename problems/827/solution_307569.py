def qtd_divisores(n):
    '''
    Programa que lê um inteiro positivos n e verifica e imprime uma
    mensagem indicando se n é perfeito.
    '''
=
    # leia o valor de n
 =
    soma = 0
  
    for divisor in range(1,n):
        while n % divisor == 0:
            soma += divisor # soma = soma + divisor
            return soma