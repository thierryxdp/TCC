def soma_h(termo):
    """ função que recebe um termo como entrada, calcula e retorna o valor de uma icógnita
    com n termos, onde n é inteiro. int --> int """
    soma = 0
    n = 1
    while n <= termo:
        soma += (1/n)
        n += 1
    return round(soma, 2)