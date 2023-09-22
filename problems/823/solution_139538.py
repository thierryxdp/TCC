def faltante(lista):
    '''Recebe uma lista com N peças numeradas, com uma peça faltando, de
    1 a N e retorna a que estiver faltando (list -> N)'''
    ordenados = lista.sort()
    proximo = 1
    while proximos < len(ordenados):
        if ordenados[proximo] - 1 != ordenados[proximo - 1]:
            return ordenados[proximo] + 1
        proximo = proximo + 1