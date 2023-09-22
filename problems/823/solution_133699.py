def faltante(lis):
    i = 0
    faltando = 0
    while(faltando == 0 and i < len(lis)-1):
        if(lis[i+1] == (lis[i]+1)):
            i += 1
        else:
            faltando = i
    return i