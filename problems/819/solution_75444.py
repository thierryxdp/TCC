def filtraMultiplos(l,n):
    x = 0
    while x < len(l):
        if l[x]%n!=0:
            return l.pop(x)
        else:
            x = x + 1
            return l