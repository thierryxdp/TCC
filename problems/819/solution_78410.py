def filtraMultiplos(L,N):
    ct = 0
    f = []
    while ct < len(L):
        if L[ct]%N == 0:
        	f = f + (L[ct],)
        ct = ct+1
    return f