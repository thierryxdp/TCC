def faltante(pecas):
    #função que mostra a peça que falta no quebra-cabeça
    #[] -> int
    contador = 1
    N = len(pecas)
    while contador <= N+1:
        if contador not in pecas:
            return contador
        contador = contador+1