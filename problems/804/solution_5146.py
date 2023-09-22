def filtra_pares(numeros):
    tupla_saida =()
    for numero in numeros:
        if numero%2 == 0:
            tupla_saida+= (numero,)
    return tupla_saida