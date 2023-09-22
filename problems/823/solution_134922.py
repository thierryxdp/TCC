def faltante (n):
    nCrescent=sorted(n)
    i=0
    while i < len(nCrescent):
        if i+1 != nCrescent[i]:
            return i+1
        i=i+1
    return len(nCrescent) + 1