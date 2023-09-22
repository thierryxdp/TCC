def primo (n):
    if n >= 1:
        for i in range(1, n):
            if n % i != 0:
                return True
            else:
                return False