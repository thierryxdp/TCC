def filtra_pares(t):
    """funçao que recebe de entrada uma tupla com 4 inteiros
    e retorna uma nova tupla somente com elementos pares ou
    tupla vazia caso nenhum inteiro de entrada seja par
    int -> int"""
    if t[0]%2 == 0:
        a=(t[0],)
    else:
        a=()
    if t[1]%2==0:
        b=(t[1],)
    else:
        b=()
    if t[2]%2==0:
        c=(t[2],)
    else:
        c=()
    if t[3]%2==0:
        d=(t[3],)
    else:
        d=()
    return a+b+c+d