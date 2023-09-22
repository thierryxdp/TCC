def total(lista, produtos):
    soma = ()
    i = 0
    list = str.split(lista,)
    while i < len(list):
        a = produtos[lista[i]]
        soma = soma + a
        i = i + 1
    return soma