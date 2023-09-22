def soma_h(n):
    """ Essa função recebe n e retorna a soma dos valores
    até n com n como denominador. int->int."""
    soma = 0
    for i in range(n):
        resultado = 1/(1+i)
        soma = soma + resultado
    return round(soma,2)