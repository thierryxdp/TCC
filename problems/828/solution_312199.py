def primo (n):
    if n<=2:
        return True
    if n>2:
        for x in range(2, x+1):
        if n%x==0:
            return False
        else:
            return True