def primo (n):
    a = []
    for d in range(1, (n+1)):
        if n%d == 0:
            a += n
            if len(a) == 1:
                return True
            else:
                return False
        else: False