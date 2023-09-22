def soma_h(n):
    """ Dado um número de termos n, retorna a soma de 1/i com n termos, sendo i o enésimo termo
    int -> float
    """
    resultado = 0
    for i in range(1, n + 1):
        divisao = 1/i
        resultado += divisao
    return round(resultado, 2)