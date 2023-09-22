def filtraMultiplos(lista):
    n1 = int(input())
    n2 = int(input())
    count = 0
    for c in range(n1, n2, n1):
    count += 1
    return ('O numero {} tem {} multiplos menores que {}.'.format(n1, count, n2))