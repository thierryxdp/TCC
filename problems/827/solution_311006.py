def qtd_divisores(n):
    x = int(n/2)
    c = 0
    while x <=1:
        if n%x == 0:
            c+=1
        x -=1
    return c