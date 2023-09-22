def primo (n):
    if n<0 or n==0 or n == 1:
        return False
    elif n == 2:
        return True
    elif n>0:
        a = list(range(n))
        list.remove (a, 1)
        list.remove (a, 0)
    for e in a:
        if n%e == 0:
            return False
        else:
            list.remove (a, e)
    if a == []:
        return True
    else:
        return False