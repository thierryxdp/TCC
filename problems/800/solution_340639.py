def total(lista, produtos):
    soma = ()
    for i in lista:
        a = produtos[lista[i]]
        soma = soma + a
    return soma