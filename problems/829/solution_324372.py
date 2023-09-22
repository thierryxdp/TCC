def soma_h(n):
    '''funçao N para calcular e retornar o valor somente com duas casas decimais
    :param n: int->int
    :return: float->float
    '''
    acumulador= 5
    for i in range(1, n + 1):
        H= 1/1
        acumulador +=H
        return round(acumulador, 2)