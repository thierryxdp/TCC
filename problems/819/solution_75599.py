def filtraMultiplos(lista,numero):
    """Recebe uma lista e um numero e retorna outra lista com todos os numeros divisiveis pelo numero recebido; lista, int->lista"""
    posicao = 0 
    multiplos = []
    while posicao < len(lista):
        if lista[posicao] % numero == 0:
            multiplos.append(lista[posicao])
        posicao = posicao + 1
    return multiplos