def filtraMultiplos(l,n):
    x = 0
    while x < len(l):
        if l[x]%n!=0:
             l.pop(x)
        else:
            x = x+1
            return l