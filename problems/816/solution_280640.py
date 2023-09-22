def maiores(L,N):
    N = [N]
    list.sort(L)
    list.reverse(L)
    
    if L > N:
        list.reverse(L)
        return L
    else:
        return []