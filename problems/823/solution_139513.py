def faltante(l):
    if len(l)==l[len(l)-1]:
        return len(l)+1
    elif l[0]!=1:
        return 1
    for i in l:
        if l[i]!=i+1:
            return i+1