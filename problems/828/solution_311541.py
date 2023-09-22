def primos(n):
    lista=list(range(n))[2:]

    for x in lista:
        if n%x==0:
            return False
    else:
        return True