def soma_h (numero):
    '''Função que dado um número inteiro, irá retornar o valor da soma 
    dos n primeiros números 
    int -> int'''
    soma = 0
    for c in range(1, numero+1):
        inverso = 1/c
        soma = soma + inverso
    return round(soma, 2)