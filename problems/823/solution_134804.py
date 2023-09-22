def faltante(x):
    'retorna o numero ausente na lista x'
    i = 0
    lista = [0]
    while i < (len(x)+1):
        i = i + 1
        lista = lista + [i]
    return (sum(lista))-(sum(x))