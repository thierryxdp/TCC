def filtraMultiplos (n):
    '''funcao que retorna uma lista nova contendo todos os elementos da original que sao miltiplos de n'''
    n1 = ()
    n2 = ()
    soma = 0
    count = -1
    for c in range(n1, n2):
        if c % n == 0:
            soma += c
            count += 1
    return (n1, count, n2)