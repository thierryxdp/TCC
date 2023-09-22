def maiores(L,N):
    M = [N]
    L = L + M
    list.sort(L)
    Z = list.index(L,N)
    Z = Z + 1
    return L[Z:]