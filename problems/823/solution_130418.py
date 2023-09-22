def faltante(numeros):
    return list(set(range(min(numeros), max(numeros) + 1)) - set(numeros))