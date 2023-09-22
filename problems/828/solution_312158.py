def primo (n):
    i=1
    for i in range(2,n//2):
        if n % i == 0:
            i=i+1
            return False
        else:
            return True