def faltante(numeros):
    # intervalo contendo todos os números possíveis (baseado na lista de números)
    # vai do menor valor existente da lista até o maior
    intervalo = range(min(numeros), max(numeros) + 1)
    return list(set(intervalo) - set(numeros))