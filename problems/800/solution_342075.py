def total(lista,dicionario):
    valor = 0
    for item in lista:
        if item in dicionario:
            valor +=dicionario[item]
    return (valor,2)