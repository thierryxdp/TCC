def filtra_pares (a,b,c,d):
    #funçao recebe uma tupla com quatro elementos inteiros e retorna uma
    #nova tupla com elementos pares da tupla original na mesma ordem
    #int, int, int, int -> int
    n = a,b,c,d
    pares = n[0]%2==0
    for numero in n:
        if numero % 2 == 0:
            list.append(pares,numero)
    return tuple(pares)