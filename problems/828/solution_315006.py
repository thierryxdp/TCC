def primo(n):
    x = 1
    k = 0
    while x < n + 1:
        if n%x==0:
            k = k +1
        x = x + 1
    if k == 2:
        return 1==1
    else:
        return 1==0