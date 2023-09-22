def filtramultiplos(lista, n):
    '''funcao pnde recebe lista e retorna lista com numeros multiplos do numero n list, int --> list'''
    multiplos = []
    contador = 0
    while contador < len(lista):
        if lista[contador] % n ==0:
            multiplos.insert(contador, lista[contador])
            contador = contador + 1
    return multiplos