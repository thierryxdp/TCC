def qtd_divisores(numero):
    '''funcao que calcula a quantidade de divisores que um numero tem. int --> int'''
    contador = 0
    for divisor in range(numero):
        if divisor != 0:
            if numero%divisor == 0:
                contador += 1
        
    return contador