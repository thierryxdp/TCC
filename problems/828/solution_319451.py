def primos(n):
    x = n
    c = 0
    primo = false
    while x >=1:
        if n%x == 0:
            c+=1
        x -=1
    if c == 2:
        primo = true
    return primo