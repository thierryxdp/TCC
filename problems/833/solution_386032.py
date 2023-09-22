def conta_numero(numero,matriz):
    i = 0
    j = 0
    soma = 0
    while i =< len(matriz):
        while j < len(matriz[0]):
            lista = matriz[0]
            if lista[j] == numero:
                soma = soma + 1
            j = j + 1
        i = i + 1
    return soma