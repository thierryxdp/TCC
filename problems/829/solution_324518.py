def soma_h(num):
    '''Esta função calcula o somátorio de 1/n
    assinatura int -> int'''
    soma = 0
    for i in range(1, num + 1):
        soma = soma + 1/i
        return round(soma,2)