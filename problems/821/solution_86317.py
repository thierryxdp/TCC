def fatorial (n):
    "dado um número 'n', retorna o resultado de n! . int -> int"
    resultado = 1
    fator = 1
    while fator <= n:
        resultado = resultado*fator
        fator = fator + 1
    return resultado