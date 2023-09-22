def primos(n):
    for d in range(2,n):
        if n%d!=0:
            return True
        else:
            return False