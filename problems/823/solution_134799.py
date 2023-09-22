def faltante(x):
    'retorna o numero ausente na lista x'
    i = 0
    lista = [0]
    while i <= len(x):
        lista = lista + [i]
        i = i + 1
    return (sum(lista))-(sum(x))