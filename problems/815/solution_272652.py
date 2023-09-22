def insere(L,n):
    n = len(L)
    for i in range(1,n):
        x = L[i]
        j = i-1
        while j >= 0 and L[j] > x:
            L[j+1] = L[j]
            j -= 1
            
    return L[j+1] = x