def total(lista, dicio):
    soma = 0
    for elemento in lista:
        soma = soma + dicio[elemento]
    return round(soma,2)