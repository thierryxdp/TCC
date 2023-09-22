def total(lista,dicionario):
    a = 0
    contador = 0
    for produto in lista:
        soma = dicionario[lista[contador]] + a
        a = soma
        contador += 1
    return round(soma,2)