def faltante(l):
    if 1 in l:
        if max(l) == len(l)+1:
            for i in range (len(l)):
                if l[i] != i+1:
                    return i+1
        else:
            return len(l)+1
    else:
        return 1