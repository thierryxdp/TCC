def filtraMultiplos(lista, n):
    """Retorna uma lista apenas com os multiplos de n que estao na lista dada;
       Entrada:
       Saida:
    """
    posicao = 0
    multiplos = []
    while posicao < len(lista):
        if lista[posicao] == lista[posicao-1]:
            repeticao.append(1)
        posicao = posicao + 1
    return multiplos