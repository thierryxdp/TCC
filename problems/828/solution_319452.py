def primos(n):
    x = n
    c = 0
    primo = False
    while x >=1:
        if n%x == 0:
            c+=1
        x -=1
    if c == 2:
        primo = True
    return primo