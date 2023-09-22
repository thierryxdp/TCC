def filtraMultiplos(lista, n):
    '''
    Dado uma lista de números filtra os múltiplos de n.

    Uso:
    filtraMultiplos(lista, n)

    Entrada:
    - lista (list, int): Lista original
    - n  (int): Número inteiro

    Saída:
    - Retorna uma nova lista dos multiplos de n. (lista)
     '''   
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i] % n == 0:
            list.append(multiplos, lista[i])
        i = i + 1
    return multiplos