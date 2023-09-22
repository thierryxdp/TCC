def filtraMultiplos(L,n):
    '''Calcula os muliplos de n na lista L'''
    index = 0
    mult = []
     
    while index < len(L):
        if L[index]% n == 0:
            list.append(mult,L[index])
        index += 1
    return mult