def filtra_pares(a,b,c,d):
    """Função que recebe uma tupla com 4 inteiros e retorna
uma nova contendo apenas os elementos pares da original,
na mesma ordem em que se encontravam;
int, int, int, int -> tup"""
    x = a, b, c, d
    a = tup(0)
    b = tup(1)
    c = tup(2)
    d = tup(3)
    pares = (x % 2 == 0)
    return pares