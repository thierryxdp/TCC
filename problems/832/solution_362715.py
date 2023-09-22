def eh_quadrada(L):
    if L == []:
        return True
    else:
        m = len(L[0])
        n = len(L)
        if m==n:
            return True
        else:
            return False