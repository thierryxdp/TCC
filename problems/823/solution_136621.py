def faltante(pecas):
    contador = 1
    N = len(pecas)
    while contador <= N+1:
        if contador not in pecas:
            return contador
        contador = contador+1