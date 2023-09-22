def soma_h(n):
    """ Função que retorna o valor H com n termos
    int -> float """
    soma=0
    for x in range(1,n+1):
        soma=soma+(1/x)
    return round(soma,2)