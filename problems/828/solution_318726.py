def primo(num):
    prim = False
    div = 0
    for i in range(1,num+1):
        if div < 3:
            if num % i == 0:
                div += 1
    if div == 2:
        prim = True
    return prim