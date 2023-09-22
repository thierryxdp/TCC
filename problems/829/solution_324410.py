def soma_h(n):
    """funcao que calcula o valor de h com n termos onde n é inteiro e dado como entrada. retorna o resultado com apenas 2 casas decimais, usando a funcao rounds (n°, 2);
    int->float"""
    acumulador=0
    for i in range (1, n + 1):
        h = 1/i
        acumulador += H
    return round(acumulador, 2)