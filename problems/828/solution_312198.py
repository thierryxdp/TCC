def primo (n):
    if n<=2:
        return True
    if n>2:
        for x in range(2, n+1):
        if n%x==0:
            return False
        else:
            return True