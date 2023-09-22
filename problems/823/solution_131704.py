def faltante(L):
    ''''''
    i = 1
    numfalta = 0
    list.sort(L)
    if(len(L) == 1 and L[0]  == 2):
        return 1
    if (L[0] != 1):
        return 1
    while (i < len(L)):
        if((l[i] -1) == L[i-1]):
            i += 1
        else:
             numfalta = L[i] - 1
             i += 1
    if (numfalta == 0):
        numfalta = len(L) + 1
    return numfalta