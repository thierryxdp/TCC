def filtraMultiplos (lista, n):
    '''funcao que filtre os multiplos de um numero n'''
    lista= ()
    n1 = int(input())
    n2 = int(input())
    count = 0
    for n in range(n1, n2):
    if n % n1 == 0:
        count += 1
        return lista