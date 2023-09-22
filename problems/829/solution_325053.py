def soma_H(numero):
    '''Recebe um número e retorna a soma H de um somatório formado pela
    divisão do número 1 por todos os inteiros de 1 ao número 
    (int - > float).'''
    numeros = range(1, numero + 1)
    H = 0
    for N in numeros:
        H = H + (1/N)
        H_arredondado = round(H,2)