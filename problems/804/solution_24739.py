def filtra_pares(tup):
    """Função que recebe uma tupla com 4 inteiros e retorna
uma nova contendo apenas os elementos pares da original,
na mesma ordem em que se encontravam;
int, int, int, int -> tup"""
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    tup = a,b,c,d
    if a % 2 == 0:
        return a
    if b % 2 == 0:
        return b
    if a % 2 == 0 and b % 2 == 0:
        return a,b