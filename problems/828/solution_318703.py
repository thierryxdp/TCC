def primos(x):
    divisores = ()
    for divisor in range(1,x+1):
        if x%divisor == 0:
            divisores = divisores + (divisor,)
            if int(len(divisores)) = 1 or 2:
                return