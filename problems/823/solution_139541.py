def faltante(lista):
    '''Recebe uma lista com N peças numeradas, com uma peça faltando, de
    1 a N e retorna a que estiver faltando (list -> N)'''
    lista.sort()
    proximo = 1
    while proximo < len(lista):
        if lista[proximo] - 1 != lista[proximo - 1]:
            return lista[proximo] + 1
    proximo = proximo + 1