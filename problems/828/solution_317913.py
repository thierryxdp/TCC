def primo (n):
    if n<0 or n==0 or n == 1:
        return False
    elif n == 2:
        return True
    elif n>0:
        a = list(range(n))
        list.remove (a, 1)
    for e in a:
        if e%2==0:
            list.remove (a, e)
        else:
            a=a
    for e in a:
        if n%e != 0:
            list.remove (a, e)
        else:
            a=a
    if e == []:
        return True
    else:
        return False