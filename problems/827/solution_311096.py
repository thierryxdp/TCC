def qtd_divisores(numero):
    '''funcao que calcula a quantidade de divisores que um numero tem. int --> int'''
    contador = 0
    alcance = range(numero)
    testes = alcance.remove(0)
    for divisor in testes:
        if numero%divisor == 0:
            contador += 1
    return contador