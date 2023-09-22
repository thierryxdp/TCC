def primo(n):
    primos=[]

    for a in range(1,n + 1):
        if n % a == 0:
            primos.append(a)
        else:
            pass
    if len(primos) == 2:
        return True
    else:
        return False