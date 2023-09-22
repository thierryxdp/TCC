def filtra_pares (num):
    #funçao recebe uma tupla com quatro elementos inteiros e retorna uma
    #nova tupla com elementos pares da tupla original na mesma ordem
    #int, int, int, int -> int
    num = a,b,c,d
    pares = ()
    if num[0]%2==0:
        pares = pares + (num[0],)
    if num[1]%2==0:
        pares = pares + (num[1],)
    if num[2]%2==0:
        pares = pares + (num[2],)
    if num[3]%2==0:
        pares = pares + (num[3],)
    return pares