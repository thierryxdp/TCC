def filtra_pares(tup):
    """Recebe uma tupla com 4 elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os elementos pares da tupla original."""
    A,B,C,D= tup
    a=int(A)
    b=int(B)
    c=int(C)
    d=int(D)
    tuplapares=()
    if (a%2==0):
        tuplapares=tuplapares+(a,)
    if (b%2==0):
        tuplapares=tuplapares+(b,)
    if (c%2==0):
        tuplapares=tuplapares+(c,)
    if (d%2==0):
        tuplapares=tuplapares+(d,)
    return tuplapares